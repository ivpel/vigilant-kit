import unittest
from unittest.mock import MagicMock, patch

from vigilant.actions.vigilant_actions import VigilantActions
from vigilant.driver.config import Config


class InputLoggingTests(unittest.TestCase):
    def setUp(self):
        self.driver = MagicMock()
        self.driver.find_element.return_value.is_displayed.return_value = True
        self.actions = VigilantActions(self.driver, config=Config(wait_timeout=0))
        self.secret = 'private-input-937'

    def test_input_values_are_omitted_from_logs_but_reach_driver(self):
        for method in ('fill_field', 'fill_form', 'send_keys', 'type_in_alert', 'set_cookie',
                       'execute_js_script', 'execute_async_js_script', 'press_key'):
            with self.subTest(method=method):
                self.driver.reset_mock()
                with patch('vigilant.actions.vigilant_actions.ActionChains') as chains:
                    with self.assertLogs('vigilant.logger', level='DEBUG') as logs:
                        if method == 'fill_form':
                            self.actions.fill_form({'#password': self.secret})
                        elif method == 'set_cookie':
                            self.actions.set_cookie({'name': 'session', 'value': self.secret})
                        elif method.startswith('execute_'):
                            getattr(self.actions, method)('return "' + self.secret + '"', [self.secret])
                        elif method in ('type_in_alert', 'press_key'):
                            getattr(self.actions, method)(self.secret)
                        else:
                            getattr(self.actions, method)('#password', self.secret)
                    self.assertNotIn(self.secret, '\n'.join(logs.output))
                    if method in ('fill_field', 'fill_form', 'send_keys'):
                        self.driver.find_element.return_value.send_keys.assert_called_once_with(self.secret)
                        self.assertIn('#password', '\n'.join(logs.output))
                    elif method == 'type_in_alert':
                        self.driver.switch_to.alert.send_keys.assert_called_once_with(self.secret)
                    elif method == 'set_cookie':
                        self.driver.add_cookie.assert_called_once_with({'name': 'session', 'value': self.secret})
                    elif method == 'press_key':
                        chains.return_value.send_keys.assert_called_once_with(self.secret)
                        chains.return_value.send_keys.return_value.perform.assert_called_once_with()
                    else:
                        native_method = 'execute_script' if method == 'execute_js_script' else 'execute_async_script'
                        getattr(self.driver, native_method).assert_called_once_with('return "' + self.secret + '"', self.secret)

    def test_value_and_attribute_waits_omit_expected_value(self):
        self.driver.find_element.return_value.get_attribute.return_value = self.secret
        with self.assertLogs('vigilant.logger', level='DEBUG') as logs:
            self.actions.waiter.wait_for_text_to_be_present_in_element_value('#password', self.secret)
            self.actions.waiter.wait_for_text_to_be_present_in_element_attribute('#password', 'value', self.secret)
        self.assertNotIn(self.secret, '\n'.join(logs.output))
        self.assertIn('#password', '\n'.join(logs.output))
