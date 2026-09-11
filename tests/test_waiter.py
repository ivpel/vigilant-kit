import unittest
from unittest.mock import MagicMock

from selenium.common.exceptions import TimeoutException

from vigilant.actions.finder import Finder
from vigilant.actions.waiter import Waiter


class AttributeWaitTests(unittest.TestCase):
    def setUp(self):
        self.driver = MagicMock()
        self.element = self.driver.find_element.return_value
        self.waiter = Waiter(self.driver, Finder(self.driver), timeout=0)

    def test_waits_for_text_in_named_attribute(self):
        self.element.get_attribute.side_effect = lambda name: 'is-ready' if name == 'data-state' else None
        result = self.waiter.wait_for_text_to_be_present_in_element_attribute('#item', 'data-state', 'ready')
        self.assertIs(result, self.waiter)

    def test_missing_or_mismatched_attribute_times_out(self):
        for value in (None, 'loading'):
            with self.subTest(value=value):
                self.element.get_attribute.return_value = value
                with self.assertRaises(TimeoutException):
                    self.waiter.wait_for_text_to_be_present_in_element_attribute('#item', 'data-state', 'ready')
