from selenium.webdriver import Remote
from selenium.webdriver.common.by import By


class Finder:
    def __init__(self, driver):
        self.driver: Remote = driver

    def by_xpath_or_css(self, selector: str):
        """
        Return tuple with search pattern (XPATH or CSS) and searched selector.
        :param selector:
        :return:
        """
        if selector.startswith('//'):
            return By.XPATH, selector
        else:
            return By.CSS_SELECTOR, selector

    def find_multiply_by_xpath(self, selector: str):
        """
        :param selector:
        :return:
        """
        return self.driver.find_elements(By.XPATH, selector)

    def find_multiply_by_css(self, selector: str):
        """
        :param selector:
        :return:
        """
        return self.driver.find_elements(By.CSS_SELECTOR, selector)

    def find(self, selector):
        """
        Find element by XPATH or CSS selector.
        Using the * operator to "unpack" the arguments
        :param selector:
        :return:
        """
        return self.driver.find_element(*self.by_xpath_or_css(selector))

    def find_multiply(self, selector: str):
        """
        Find multiply elements using XPATH or CSS selectors.
        :param selector:
        :return:
        """
        if selector.startswith('//'):
            return self.find_multiply_by_xpath(selector)
        else:
            return self.find_multiply_by_css(selector)

    def find_by_class(self, selector):
        """
        :param selector:
        :return:
        """
        return self.driver.find_element(By.CLASS_NAME, selector)
