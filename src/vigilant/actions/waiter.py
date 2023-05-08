import os
import time

from selenium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from vigilant.actions.finder import Finder
from vigilant.logger import logger as log


def get_timeout():
    return float(os.environ.get('WAIT_TIMEOUT'))


class Waiter:

    def __init__(self, driver, finder):
        self.driver: Remote = driver
        self.finder: Finder = finder

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
        log.info(f"Waiting for element with selector: {selector} - to disappear.")
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
        log.info(f"Waiting for element with selector: {selector} - to disappear.")
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
        log.info(f"Waiting for element with selector: {selector} - to disappear.")
        WebDriverWait(driver=self.driver, timeout=get_timeout()).until(
            EC.text_to_be_present_in_element_attribute(self.finder.by_xpath_or_css(selector), text_in_attribute)
        )
        return self

    def wait_for_alert_(self, selector: str):
        """
        Waits for an alert to be present.

        :param selector: The element's selector
        :return: self
        """
        log.info(f"Waiting for element with selector: {selector} - to disappear.")
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
