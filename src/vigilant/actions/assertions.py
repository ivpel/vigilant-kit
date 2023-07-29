from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Remote

from vigilant.actions.finder import Finder
from vigilant.actions.waiter import Waiter
from vigilant.logger import logger as log

RED = "\033[31m"
RESET = "\033[0m"

class Assertions:

    def __init__(self, driver):
        self.driver: Remote = driver
        self.finder: Finder = Finder(self.driver)
        self.waiter: Waiter = Waiter(self.driver, self.finder)

    def count_visible_elements(self, selector: str) -> int:
        """
        Count visible elements that match the provided selector.

        :param selector: CSS selector
        :return: number of visible elements that match the selector
        """
        try:
            if self.finder.find(selector).is_displayed():
                return len(self.finder.find_multiply(selector))
        except NoSuchElementException:
            return 0

    def count_elements(self, selector: str) -> int:
        """
        Count all elements that match the provided selector, visible or not.

        :param selector: CSS selector
        :return: number of elements that match the selector
        """
        try:
            return len(self.finder.find_multiply(selector))
        except NoSuchElementException:
            return 0

    def dont_see(self, selectors: [str | list]) -> None:
        """
        Assert that none of the elements matching the provided selectors are visible.

        :param selectors: list of CSS selectors
        """
        if isinstance(selectors, list):
            for element in selectors:
                log.info(f"Assert: don't see element with selector {element}")
                assert self.count_visible_elements(element) == 0,\
                    f"{RED}Expected 0 elements with selector {element}, but found {self.count_visible_elements(element)}{RESET}"
        else:
            log.info(f"Assert: don't see element with selector {selectors}")
            assert self.count_visible_elements(selectors) == 0, \
                f"{RED}Expected 0 elements with selector {selectors}, but found {self.count_visible_elements(selectors)}{RESET}"

    def dont_see_in_title(self, search_key: str) -> None:
        """
        Assert that the provided search key is not present in the current page title.

        :param search_key: string to search for
        """
        log.info(f"Assert: don't see string {search_key} in current page title")
        assert search_key not in self.driver.title, \
            f"{RED}String {search_key} expected to be missing in current page title, but it appears{RESET}"

    def dont_see_in_current_url(self, search_key: str) -> None:
        """
        Assert that the provided search key is not present in the current page URL.

        :param search_key: string to search for
        """
        log.info(f"Assert: don't see string {search_key} in current page URL")
        assert search_key not in self.driver.current_url, \
            f"{RED}String {search_key} expected to to be missing in current page URL, but it appear{RESET}"

    def see(self, selectors: [str | list]) -> None:
        """
        Assert that at least one of the elements matching the provided selectors is visible.

        :param selectors: list of CSS selectors
        """
        if isinstance(selectors, list):
            for element in selectors:
                log.info(f"Assert: see element with selector {element}")
                assert self.count_visible_elements(element) > 0,\
                    f"{RED}Expected 1 element with selector {element}, but found {self.count_visible_elements(element)}{RESET}"
        else:
            log.info(f"Assert: see element with selector {selectors}")
            assert self.count_visible_elements(selectors) > 0, \
                f"{RED}Expected 1 element with selector {selectors}, but found {self.count_visible_elements(selectors)}{RESET}"

    def see_elements_in_quantity_of(self, selector: str, qty: int):
        """
        Assert that the number of visible elements that match the provided selector is equal to the provided quantity.

        :param selector: CSS selector
        :param qty: expected number of elements
        """
        log.info(f"Assert: see elements with selector {selector} in quantity of {qty}")
        assert qty == self.count_visible_elements(selector), \
            f"{RED}Expected {qty} elements with selector {selector}, but found {self.count_visible_elements(selector)}{RESET}"

    def see_at_least_one(self, selector):
        """
        Assert that at least one element matching the provided selector is visible.

        :param selector: CSS selector
        """
        log.info(f"Assert: see at least 1 element with selector {selector}")
        assert self.count_visible_elements(selector) > 1, \
            f"{RED}Expected quantity of elements with selector {selector} be at least 1, but found {self.count_visible_elements(selector)}{RESET}"

    def see_in_title(self, search_key):
        """
        Assert that the provided search key is present in the current page title.

        :param search_key: string to search for
        """
        log.info(f"Assert: see string {search_key} in current page title")
        assert search_key in self.driver.title, \
            f"{RED}String {search_key} expected to be in current page title, but it is missing{RESET}"

    def see_in_url(self, search_key: str):
        """
        Assert that the provided search key is present in the current page URL.

        :param search_key: string to search for
        """
        log.info(f"Assert: see string {search_key} in current page URL")
        assert search_key in self.driver.current_url, \
            f"{RED}String {search_key} expected to be in current page URL, but it is missing{RESET}"

    def see_text(self, text):
        """
        Assert that the provided text is present on the current page.

        :param text: text to search for
        """
        selector_with_text = '//*[text()="' + text + '"]'
        assert self.count_visible_elements(selector_with_text) > 0,\
            f"{RED}Text {text} was not found on the current page{RESET}"
