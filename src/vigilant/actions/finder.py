from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from typing import Tuple, List
from selenium.webdriver.remote.webelement import WebElement


class Finder:
    def __init__(self, driver: Remote):
        """
        Initialize Finder with the Selenium WebDriver.

        :param driver: Selenium WebDriver instance
        """
        self.driver: Remote = driver

    def by_xpath_or_css(self, selector: str) -> Tuple[str, str]:
        """
        Return tuple with search pattern (XPATH or CSS) and searched selector.

        :param selector: XPATH or CSS selector string
        :return: tuple with search pattern (XPATH or CSS) and searched selector
        """
        if selector.startswith('//'):
            return By.XPATH, selector
        else:
            return By.CSS_SELECTOR, selector

    def find_multiply_by_xpath(self, selector: str) -> List[WebElement]:
        """
        Find multiple elements by XPATH selector.

        :param selector: XPATH selector string
        :return: list of elements found using the XPATH selector
        """
        return self.driver.find_elements(By.XPATH, selector)

    def find_multiply_by_css(self, selector: str) -> List[WebElement]:
        """
        Find multiple elements by CSS selector.

        :param selector: CSS selector string
        :return: list of elements found using the CSS selector
        """
        return self.driver.find_elements(By.CSS_SELECTOR, selector)

    def find(self, selector: str) -> WebElement:
        """
        Find element by XPATH or CSS selector.
        Using the * operator to "unpack" the arguments.

        :param selector: XPATH or CSS selector string
        :return: the element found using the XPATH or CSS selector
        """
        return self.driver.find_element(*self.by_xpath_or_css(selector))

    def find_multiply(self, selector: str) -> List[WebElement]:
        """
        Find multiple elements using XPATH or CSS selectors.

        :param selector: XPATH or CSS selector string
        :return: list of elements found using the XPATH or CSS selector
        """
        if selector.startswith('//'):
            return self.find_multiply_by_xpath(selector)
        else:
            return self.find_multiply_by_css(selector)

    def find_by_class(self, selector: str) -> WebElement:
        """
        Find element by class name.

        :param selector: class name string
        :return: the element found using the class name selector
        """
        return self.driver.find_element(By.CLASS_NAME, selector)
