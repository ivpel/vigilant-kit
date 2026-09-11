from contextlib import asynccontextmanager
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import trio
from trio.testing import MockClock
from selenium.common.exceptions import WebDriverException

from vigilant.actions.assertions import Assertions
from vigilant.actions.finder import Finder
from vigilant.actions.waiter import Waiter
from vigilant.bidi import BiDiUnavailableError
from vigilant.bidi._bidi import VigilantBiDi
from vigilant.driver.config import Config


class Receiver:
    def __init__(self, events=()):
        self.events = iter(events)
        self.closed = False

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        self.closed = True

    def __aiter__(self):
        return self

    async def __anext__(self):
        return await self.receive()

    async def receive(self):
        event = next(self.events, None)
        if event is None:
            await trio.sleep_forever()
        delay, value = event
        await trio.sleep(delay)
        return value


class Session:
    def __init__(self, events=None):
        self.events = events or {}
        self.receivers = []

    async def execute(self, command):
        pass

    def listen(self, event_type, **kwargs):
        receiver = Receiver(self.events.get(event_type, ()))
        self.receivers.append(receiver)
        return receiver


class Driver:
    def __init__(self, events=None, connection_error=None):
        self.session = Session(events)
        self.connection_error = connection_error
        self.closed = False

    @asynccontextmanager
    async def bidi_connection(self):
        if self.connection_error:
            raise self.connection_error
        network = SimpleNamespace(
            enable=lambda: None, ResponseReceived='response', RequestWillBeSent='request',
            LoadingFinished='finished', LoadingFailed='failed',
        )
        runtime = SimpleNamespace(enable=lambda: None, ConsoleAPICalled='console', ExceptionThrown='exception')
        try:
            yield SimpleNamespace(session=self.session, devtools=SimpleNamespace(network=network, runtime=runtime))
        finally:
            self.closed = True


class BiDiTests(unittest.TestCase):
    def setUp(self):
        self.clock = MockClock(autojump_threshold=0)
        runner = patch('vigilant.bidi._bidi._trio_run', side_effect=lambda fn: trio.run(fn, clock=self.clock))
        runner.start()
        self.addCleanup(runner.stop)

    def waiter(self, driver):
        return Waiter(driver, Finder(driver), timeout=2)

    def test_unavailable_connections_raise_by_default(self):
        for driver in (SimpleNamespace(), Driver(connection_error=OSError('offline')),
                       Driver(connection_error=WebDriverException('unavailable'))):
            with self.subTest(driver=driver), self.assertRaises(BiDiUnavailableError):
                self.waiter(driver).wait_for_response(url_contains='/api')

    def test_explicit_warning_policy_logs_once_and_skips(self):
        driver = Driver(connection_error=OSError('offline'))
        waiter = self.waiter(driver)
        with self.assertLogs('vigilant.logger', level='WARNING') as logs:
            self.assertIs(waiter.wait_for_response(url_contains='/api', on_unavailable='warn'), waiter)
            waiter.wait_for_network_idle(on_unavailable='warn')
        self.assertEqual(len(logs.output), 1)

    def test_operation_errors_propagate_even_with_warning_policy(self):
        for error in (ValueError('bug'), AssertionError('failed'), OSError('lost connection'),
                      WebDriverException('command failed')):
            with self.subTest(error=error):
                driver = Driver()

                async def fail(bidi):
                    raise error

                with self.assertRaises(type(error)):
                    VigilantBiDi(driver).run(fail, on_unavailable='warn')
                self.assertTrue(driver.closed)

    def test_unexpected_setup_errors_are_not_skipped(self):
        with self.assertRaises(ValueError):
            self.waiter(Driver(connection_error=ValueError('bug'))).wait_for_network_idle(on_unavailable='warn')

    def test_invalid_policy_is_rejected(self):
        with self.assertRaises(ValueError):
            self.waiter(Driver()).wait_for_network_idle(on_unavailable='ignore')

    def test_response_timeout_is_not_skipped(self):
        driver = Driver()
        with self.assertRaises(trio.TooSlowError):
            self.waiter(driver).wait_for_response(url_contains='/api', on_unavailable='warn')
        self.assertTrue(driver.closed)
        self.assertTrue(all(receiver.closed for receiver in driver.session.receivers))

    def test_response_matches_url_and_status(self):
        def response(url, status):
            return SimpleNamespace(response=SimpleNamespace(url=url, status=status))

        driver = Driver({'response': [(0, response('/other', 200)), (0, response('/api', 500)),
                                      (0.2, response('/api', 200))]})
        waiter = self.waiter(driver)
        self.assertIs(waiter.wait_for_response(url_equals='/api', status=200), waiter)
        self.assertTrue(driver.closed)

    def test_idle_returns_before_timeout_and_closes_listeners(self):
        driver = Driver()
        waiter = self.waiter(driver)
        self.assertIs(waiter.wait_for_network_idle(idle_ms=100), waiter)
        self.assertLess(self.clock.current_time(), 2)
        self.assertEqual(len(driver.session.receivers), 3)
        self.assertTrue(all(receiver.closed for receiver in driver.session.receivers))
        self.assertTrue(driver.closed)

    def test_idle_waits_for_requests_to_finish_or_fail(self):
        for completion in ('finished', 'failed'):
            with self.subTest(completion=completion):
                request = SimpleNamespace(request_id='one')
                driver = Driver({'request': [(0, request)], completion: [(0.5, request)]})
                started = self.clock.current_time()
                self.waiter(driver).wait_for_network_idle(idle_ms=100)
                self.assertGreaterEqual(self.clock.current_time() - started, 0.6)
                self.assertTrue(all(receiver.closed for receiver in driver.session.receivers))

    def test_unfinished_request_times_out_and_closes_listeners(self):
        driver = Driver({'request': [(0, SimpleNamespace(request_id='one'))]})
        with self.assertRaises(trio.TooSlowError):
            self.waiter(driver).wait_for_network_idle(on_unavailable='warn')
        self.assertTrue(all(receiver.closed for receiver in driver.session.receivers))

    def test_console_and_js_checks_fail_on_errors(self):
        for method, event_type, event in (
            ('no_console_errors', 'console', SimpleNamespace(type_='error', args=[SimpleNamespace(value='boom')])),
            ('no_js_errors', 'exception', SimpleNamespace(exception_details=SimpleNamespace(text='boom'))),
        ):
            with self.subTest(method=method):
                checks = Assertions(Driver({event_type: [(0, event)]}), config=Config())
                with self.assertRaisesRegex(AssertionError, 'boom'):
                    getattr(checks, method)(on_unavailable='warn')

    def test_assertion_unavailability_policy(self):
        for method in ('no_console_errors', 'no_js_errors'):
            with self.subTest(method=method):
                checks = Assertions(SimpleNamespace(), config=Config())
                with self.assertRaises(BiDiUnavailableError):
                    getattr(checks, method)()
                with self.assertLogs('vigilant.logger', level='WARNING'):
                    getattr(checks, method)(on_unavailable='warn')
