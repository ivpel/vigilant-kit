import os
import unittest
from urllib.parse import quote

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from vigilant.actions.vigilant_actions import VigilantActions
from vigilant.driver.config import Config


@unittest.skipUnless(os.environ.get('VIGILANT_BROWSER_TESTS') == '1', 'opt-in Chrome integration tests')
class ChromeRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(options=options)
        cls.addClassCleanup(cls.driver.quit)
        cls.browser = VigilantActions(cls.driver, config=Config(wait_timeout=2))

    def setUp(self):
        html = '''<html><body>
            <div class="item" hidden>Hidden</div><div class="item">Visible</div>
            <div class="reverse">Visible</div><div class="reverse" hidden>Hidden</div>
            <div id="state" data-state="loading">Status</div>
        </body></html>'''
        self.driver.get('data:text/html;charset=utf-8,' + quote(html))

    def test_mixed_visibility_assertions(self):
        for selector in ('.item', '.reverse'):
            with self.subTest(selector=selector):
                self.browser.assertions.see_element(selector)
                self.browser.assertions.see_elements_in_quantity_of(selector, 1)
                with self.assertRaises(AssertionError):
                    self.browser.assertions.dont_see(selector)
        self.browser.assertions.dont_see('.missing')

    def test_attribute_wait_observes_dynamic_change(self):
        self.driver.execute_script("setTimeout(() => document.querySelector('#state').setAttribute('data-state', 'ready'), 100)")
        self.browser.waiter.wait_for_text_to_be_present_in_element_attribute('#state', 'data-state', 'ready')

    def test_attribute_wait_rejects_wrong_value(self):
        with self.assertRaises(TimeoutException):
            self.browser.waiter.wait_for_text_to_be_present_in_element_attribute('#state', 'data-state', 'ready')
