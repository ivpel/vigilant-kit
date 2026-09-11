import unittest
from unittest.mock import MagicMock

from vigilant.actions.assertions import Assertions
from vigilant.driver.config import Config


class VisibilityTests(unittest.TestCase):
    def checks_for(self, states):
        driver = MagicMock()
        elements = [MagicMock() for _ in states]
        for element, visible in zip(elements, states):
            element.is_displayed.return_value = visible
        driver.find_elements.return_value = elements
        driver.find_element.return_value = elements[0] if elements else None
        return Assertions(driver, config=Config(wait_timeout=0))

    def test_counts_each_elements_visibility(self):
        for states in ([], [False], [True], [False, True], [True, False], [True, True]):
            with self.subTest(states=states):
                self.assertEqual(self.checks_for(states).count_visible_elements('.item'), sum(states))

    def test_dont_see_fails_when_later_match_is_visible(self):
        with self.assertRaises(AssertionError):
            self.checks_for([False, True]).dont_see('.item')

    def test_see_element_accepts_visible_later_match(self):
        self.checks_for([False, True]).see_element('.item')

    def test_quantity_excludes_hidden_matches(self):
        self.checks_for([True, False]).see_elements_in_quantity_of('.item', 1)

    def test_dont_see_accepts_absent_and_hidden_elements(self):
        for states in ([], [False, False]):
            with self.subTest(states=states):
                self.checks_for(states).dont_see('.item')
