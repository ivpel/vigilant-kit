import os

from selenium.webdriver import Remote
from selenium.webdriver.common.action_chains import ActionChains

from vigilant.actions.assertions import Assertions
from vigilant.actions.finder import Finder
from vigilant.actions.waiter import Waiter
from vigilant.logger import logger as log


def get_base_url():
    return os.environ.get('BASE_URL')


class VigilantActions:
    """
    `VigilantActions` - provide methods for interaction with browser. This is wrapper on native Selenium WebDriver
    methods for working with browser in more comfortable way, with smart waiters, finders and assertions.
    `waiter` - smart wait methods.
    `finder` - methods for comfortable elements search.
    `assertions` - assertion methods for browser.
    """

    def __init__(self, driver):
        self.driver: Remote = driver
        self.assertions: Assertions = Assertions(self.driver)
        self.finder: Finder = Finder(self.driver)
        self.waiter: Waiter = Waiter(self.driver, self.finder)

    def get_page(self, url):
        """
        Opens the page by the URL relative to the one set in the BASE_URL configuration variable.
        Args:
            url: A path to the page relative to the BASE_URL
        :return:
        """
        log.info(f'Getting page: {url}')
        self.driver.get(get_base_url() + url)
        return self

    def close(self):
        log.info(f'Closing the current window')
        self.driver.close()
        return self

    def quit(self):
        log.info(f'Quits the driver and closes every associated window')
        self.driver.quit()
        return self

    def page_back(self):
        log.info(f'Goes one step backward in the browser history')
        self.driver.back()
        return self

    def page_forward(self):
        log.info(f'Goes one step forward in the browser history')
        self.driver.forward()
        return self

    def page_refresh(self):
        log.info(f'Refreshes the current page')
        self.driver.refresh()
        return self

    def get_page_title(self):
        log.info(f'Returns the title of the current page')
        return self.driver.title

    def maximize_window(self):
        log.info(f'Maximizes the current window that webdriver is using')
        self.driver.maximize_window()
        return self

    def resize_window(self, width, height):
        log.info(f'Sets current window width to: {width}px and height to: {height}px')
        self.driver.set_window_size(width, height)
        return self

    def execute_js_script(self, js_script, arguments=None):
        log.info(f'Execute JS script: {js_script} with arguments: {arguments}')
        self.driver.execute_script(js_script, arguments)
        return self

    def execute_async_js_script(self, js_script, arguments=None):
        log.info(f'Execute async JS script: {js_script} with arguments: {arguments}')
        self.driver.execute_async_script(js_script, arguments)
        return self

    def delete_all_cookies(self):
        log.info(f'Delete all cookies in the scope of the session')
        self.driver.delete_all_cookies()
        return self

    def delete_cookie(self, cookie_to_delete):
        log.info(f'Deleting cookie: {cookie_to_delete}')
        self.driver.delete_cookie(cookie_to_delete)
        return self

    def set_cookie(self, cookie_name: dict):
        log.info(f'Setting cookie: {cookie_name}')
        self.driver.add_cookie(cookie_name)

    def get_all_cookies(self):
        log.info(f'Returns a set of dictionaries, corresponding to cookies visible in the current session')
        self.driver.get_cookies()
        return self

    def get_cookie(self, cookie):
        log.info(f' Get a single cookie: {cookie}')
        self.driver.get_cookie(cookie)
        return self

    def switch_to_frame(self, frame_id):
        log.info(f'Switching to frame: {frame_id}')
        self.driver.switch_to.frame(frame_id)
        return self

    def switch_to_default(self):
        log.info(f'Switching focus to the default frame')
        self.driver.switch_to.default_content()
        return self

    def dismiss_alert(self):
        log.info(f'Dismissing the alert')
        self.driver.switch_to.alert.dismiss()
        return self

    def accept_alert(self):
        log.info(f'Accepting alert')
        self.driver.switch_to.alert.accept()
        return self

    def type_in_alert(self, value):
        log.info(f'Typing in alert: {value}')
        self.driver.switch_to.alert.text(value)
        return self

    def click_with_delay(self, selector, delay=2):
        """
        CLick on element only after it become visible and + 2 additional seconds of waiting, after it become visible.
        argument delay has default value of 2 but can be changed.
        :param selector:
        :param delay:
        :return:
        """
        self.waiter.wait_for_element_to_be_visible(selector)
        self.waiter.strict_wait(delay)
        log.info(f'Clicking on element: {selector} with delay: {delay}')
        self.finder.find(selector).click()

    def click(self, selector):
        self.waiter.wait_for_element_to_be_visible(selector)
        log.info(f'Clicking on element: {selector}')
        self.finder.find(selector).click()

    def scroll_to(self, selector):
        target = self.finder.find(selector)
        log.info(f'Scrolling to element: {selector}')
        self.execute_js_script('arguments[0].scrollIntoView({block: "center"})', target)

    def get_text_from_element(self, selector):
        self.waiter.wait_for_element_to_be_visible(selector)
        log.info(f'Getting text from element: {selector}')
        return self.finder.find(selector).text

    def fill_field(self, selector, value):
        self.waiter.wait_for_element_to_be_visible(selector)
        log.info(f'Filling field: {selector} with value: {value}')
        self.finder.find(selector).send_keys(value)
        return self

    def move_mouse_on_element(self, selector):
        self.waiter.wait_for_element_to_be_visible(selector)
        element = self.finder.find(selector)
        log.info(f'Moving mouse on element: {selector}')
        ActionChains(self.driver).move_to_element(element)
        return self

    def press_key(self, key):
        log.info(f'Pressing key: {key}')
        actions = ActionChains(self.driver)
        actions.send_keys(key).perform()
        return self

    def send_keys(self, selector, keys):
        log.info(f'Send keys: {keys} to the field: {selector}')
        self.finder.find(selector).send_keys(keys)
        return self

    def submit_form(self, selector):
        log.info(f'Submitting form: {selector}')
        self.finder.find(selector).submit()
        return self

    def clear_field(self, selector):
        self.waiter.wait_for_element_to_be_visible(selector)
        log.info(f'Clearing field: {selector}')
        self.finder.find(selector).clear()
