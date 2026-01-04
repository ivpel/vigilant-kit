import os
import time

from selenium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from vigilant.actions.finder import Finder
from vigilant.bidi._bidi import VigilantBiDi
from vigilant.logger import logger as log


def get_timeout(default: float = 10.0) -> float:
    """
    Fetch wait timeout from env with a safe default.

    :param default: fallback timeout if WAIT_TIMEOUT is not set
    :return: timeout in seconds
    """
    raw_timeout = os.environ.get('WAIT_TIMEOUT')
    if raw_timeout is None or raw_timeout == "":
        return default
    try:
        return float(raw_timeout)
    except ValueError as exc:
        raise ValueError(f"WAIT_TIMEOUT must be numeric, got: {raw_timeout}") from exc


class Waiter:

    def __init__(self, driver, finder):
        self.driver: Remote = driver
        self.finder: Finder = finder
        self._bidi = VigilantBiDi(self.driver)

    def wait_for_element_to_be_clickable(self, selector: str):
        """
        Waits for the element with the specified selector to be clickable.

        :param selector: The element's selector
        :return: self
        """
        log.info(f"Waiting for element with selector: {selector} - to be clickable.")
        WebDriverWait(driver=self.driver, timeout=get_timeout()).until(
            EC.element_to_be_clickable(self.finder.by_xpath_or_css(selector))
        )
        return self

    def wait_for_element_to_be_visible(self, selector: str):
        """
        Waits for the element with the specified selector to be visible.

        :param selector: The element's selector
        :return: self
        """
        log.info(f"Waiting for element with selector: {selector} - to be visible.")
        WebDriverWait(driver=self.driver, timeout=get_timeout()).until(
            EC.visibility_of_element_located(self.finder.by_xpath_or_css(selector))
        )
        return self

    def wait_for_element_to_be_present_in_dom(self, selector: str):
        """
        Waits for the element with the specified selector to be present in the DOM.

        :param selector: The element's selector
        :return: self
        """
        log.info(f"Waiting for element with selector: {selector} - to be presented in DOM.")
        WebDriverWait(driver=self.driver, timeout=get_timeout()).until(
            EC.presence_of_element_located(self.finder.by_xpath_or_css(selector))
        )
        return self

    def wait_for_element_to_disappear(self, selector: str):
        """
        Waits for the element with the specified selector to disappear.

        :param selector: The element's selector
        :return: self
        """
        log.info(f"Waiting for element with selector: {selector} - to disappear.")
        WebDriverWait(driver=self.driver, timeout=get_timeout()).until(
            EC.invisibility_of_element_located(self.finder.by_xpath_or_css(selector))
        )
        return self

    def wait_for_text_to_be_present_in_element_value(self, selector: str, value_text: str):
        """
        Waits for the specified text to be present in the value of the element with the given selector.

        :param selector: The element's selector
        :param value_text: The text to wait for
        :return: self
        """
        log.info(f"Waiting for element with selector: {selector} - to contain value: {value_text}.")
        WebDriverWait(driver=self.driver, timeout=get_timeout()).until(
            EC.text_to_be_present_in_element_value(self.finder.by_xpath_or_css(selector), value_text)
        )
        return self

    def wait_for_text_to_be_present_in_element(self, selector: str, text: str):
        """
        Waits for the specified text to be present in the element with the given selector.

        :param selector: The element's selector
        :param text: The text to wait for
        :return: self
        """
        log.info(f"Waiting for element with selector: {selector} - to contain text: {text}.")
        WebDriverWait(driver=self.driver, timeout=get_timeout()).until(
            EC.text_to_be_present_in_element(self.finder.by_xpath_or_css(selector), text)
        )
        return self

    def wait_for_text_to_be_present_in_element_attribute(self, selector: str, text_in_attribute: str):
        """
        Waits for the specified text to be present in the attribute of the element with the given selector.

        :param selector: The element's selector
        :param text_in_attribute: The text to wait for
        :return: self
        """
        log.info(f"Waiting for element with selector: {selector} - to contain attribute text: {text_in_attribute}.")
        WebDriverWait(driver=self.driver, timeout=get_timeout()).until(
            EC.text_to_be_present_in_element_attribute(self.finder.by_xpath_or_css(selector), text_in_attribute)
        )
        return self

    def wait_for_alert_(self, selector=None):
        """
        Waits for an alert to be present.

        :param selector: unused, kept for backward compatibility
        :return: self
        """
        log.info("Waiting for alert to be present.")
        WebDriverWait(driver=self.driver, timeout=get_timeout()).until(
            EC.alert_is_present()
        )
        return self

    def strict_wait(self, seconds: int):
        """
        Waits for the specified number of seconds.

        :param seconds: The number of seconds to wait
        :return: self
        """
        log.info(f"Strict wait for {seconds} seconds")
        time.sleep(seconds)
        return self

    def wait_for_response(
        self,
        url_contains: str | None = None,
        url_equals: str | None = None,
        status: int | None = None,
        timeout: float | None = None,
    ):
        """
        Wait for a matching network response using Selenium's BiDi/CDP connection.

        When BiDi isn't available (common on cloud/Grid providers), this method logs a warning and skips.
        """

        timeout = get_timeout() if timeout is None else float(timeout)

        async def _wait(bidi, *, url_contains, url_equals, status, timeout):
            devtools = bidi.devtools
            session = bidi.session

            await session.execute(devtools.network.enable())
            responses = session.listen(devtools.network.ResponseReceived, buffer_size=200)

            import trio

            def _matches(event) -> bool:
                response = getattr(event, "response", None)
                if response is None:
                    return False
                url = getattr(response, "url", "") or ""
                code = getattr(response, "status", None)
                if url_equals is not None and url != url_equals:
                    return False
                if url_contains is not None and url_contains not in url:
                    return False
                if status is not None and int(code) != int(status):
                    return False
                return True

            with trio.fail_after(timeout):
                async with responses:
                    while True:
                        event = await responses.receive()
                        if _matches(event):
                            return event

        if url_contains is None and url_equals is None:
            raise ValueError("Provide at least one matcher: url_contains or url_equals")

        log.info(
            "Waiting for network response (url_contains=%s url_equals=%s status=%s timeout=%s)",
            url_contains,
            url_equals,
            status,
            timeout,
        )
        self._bidi.run(
            _wait,
            url_contains=url_contains,
            url_equals=url_equals,
            status=status,
            timeout=timeout,
        )
        return self

    def wait_for_network_idle(self, idle_ms: int = 500, timeout: float | None = None):
        """
        Wait until there are no in-flight network requests for `idle_ms`.

        Uses Selenium's BiDi/CDP connection when available; otherwise logs a warning and skips.
        """
        if idle_ms <= 0:
            raise ValueError("idle_ms must be > 0")

        timeout = get_timeout() if timeout is None else float(timeout)
        idle_seconds = idle_ms / 1000.0

        async def _wait(bidi, *, idle_seconds, timeout):
            devtools = bidi.devtools
            session = bidi.session

            await session.execute(devtools.network.enable())
            reqs = session.listen(devtools.network.RequestWillBeSent, buffer_size=500)
            finished = session.listen(devtools.network.LoadingFinished, buffer_size=500)
            failed = session.listen(devtools.network.LoadingFailed, buffer_size=500)

            import trio

            send, recv = trio.open_memory_channel(1000)

            async def _forward(receiver, kind: str):
                async with receiver:
                    async for event in receiver:
                        await send.send((kind, event))

            in_flight: set[str] = set()
            idle_started: float | None = None

            with trio.fail_after(timeout):
                async with send:
                    async with recv:
                        async with trio.open_nursery() as nursery:
                            nursery.start_soon(_forward, reqs, "req")
                            nursery.start_soon(_forward, finished, "fin")
                            nursery.start_soon(_forward, failed, "fail")

                            while True:
                                with trio.move_on_after(0.1):
                                    kind, event = await recv.receive()
                                    request_id = getattr(event, "request_id", None)
                                    if request_id is not None:
                                        request_id = str(request_id)
                                        if kind == "req":
                                            in_flight.add(request_id)
                                        else:
                                            in_flight.discard(request_id)

                                if in_flight:
                                    idle_started = None
                                else:
                                    if idle_started is None:
                                        idle_started = trio.current_time()
                                    if trio.current_time() - idle_started >= idle_seconds:
                                        return

        log.info("Waiting for network idle (idle_ms=%s timeout=%s)", idle_ms, timeout)
        self._bidi.run(_wait, idle_seconds=idle_seconds, timeout=timeout)
        return self
