from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Remote

from vigilant.actions.finder import Finder
from vigilant.actions.waiter import Waiter
from vigilant.logger import logger as log


class Assertions:

    def __init__(self, driver):
        self.driver: Remote = driver
        self.finder: Finder = Finder(self.driver)
        self.waiter: Waiter = Waiter(self.driver, self.finder)

    def count_visible_elements(self, selector):
        try:
            if self.finder.find(selector).is_displayed():
                return len(self.finder.find_multiply(selector))
        except NoSuchElementException:
            return 0

    def count_elements(self, selector):
        try:
            return len(self.finder.find_multiply(selector))
        except NoSuchElementException:
            return 0

    def dont_see(self, selectors):
        if isinstance(selectors, list):
            for element in selectors:
                log.info(f"Assert: don't see element with selector {element}")
                assert self.count_visible_elements(element) == 0,\
                    f"Expected 0 elements with selector {element}, but found {self.count_visible_elements(element)}"
        else:
            log.info(f"Assert: don't see element with selector {selectors}")
            assert self.count_visible_elements(selectors) == 0, \
                f"Expected 0 elements with selector {selectors}, but found {self.count_visible_elements(selectors)}"

    def dont_see_in_title(self, search_key: str):
        log.info(f"Assert: don't see string {search_key} in current page title")
        assert search_key not in self.driver.title, \
            f"String {search_key} expected to to be missing in current page title but it appear"

    def dont_see_in_current_url(self, search_key: str):
        log.info(f"Assert: don't see string {search_key} in current page URL")
        assert search_key not in self.driver.current_url, \
            f"String {search_key} expected to to be missing in current page URL but it appear"

    def see(self, selectors):
        if isinstance(selectors, list):
            for element in selectors:
                log.info(f"Assert: see element with selector {element}")
                assert self.count_visible_elements(element) > 0,\
                    f"Expected 1 element with selector {element}, but found {self.count_visible_elements(element)}"
        else:
            log.info(f"Assert: see element with selector {selectors}")
            assert self.count_visible_elements(selectors) > 0, \
                f"Expected 1 element with selector {selectors}, but found {self.count_visible_elements(selectors)}"

    def see_elements_in_quantity_of(self, selector: str, qty: int):
        log.info(f"Assert: see elements with selector {selector} in quantity of {qty}")
        assert qty == self.count_visible_elements(selector), \
            f"Expected {qty} elements with selector {selector}, but found {self.count_visible_elements(selector)}"

    def see_at_least_one(self, selector):
        log.info(f"Assert: see at least 1 element with selector {selector}")
        assert self.count_visible_elements(selector) > 1, \
            f"Expected quantity of elements with selector {selector} be at least 1, but found {self.count_visible_elements(selector)}"

    def see_in_title(self, search_key):
        log.info(f"Assert: see string {search_key} in current page title")
        assert search_key in self.driver.title, \
            f"String {search_key} expected to to be in current page title but it is missing"

    def see_in_url(self, search_key: str):
        log.info(f"Assert: see string {search_key} in current page URL")
        assert search_key in self.driver.current_url, \
            f"String {search_key} expected to to be in current page URL but it is missing"

    def see_text(self, text):
        selector_with_text = '//*[text()="' + text + '"]'
        assert self.count_visible_elements(selector_with_text) > 0,\
            f"Text {text} was not found on the current page"
