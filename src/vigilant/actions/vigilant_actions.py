import os

from selenium.webdriver import Remote
from selenium.webdriver.common.action_chains import ActionChains

from vigilant.actions.assertions import Assertions
from vigilant.actions.finder import Finder
from vigilant.actions.waiter import Waiter
from vigilant.logger import logger as log


def get_base_url() -> str:
    """
    Get the base URL from the environment variable 'BASE_URL'.

    :return: base URL as a string
    """
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

        :param url: A path to the page relative to the BASE_URL
        :return: self
        """
        log.info(f'Getting page: {url}')
        self.driver.get(get_base_url() + url)
        return self

    def close(self):
        """
        Closes the current window.

        :return: self
        """
        log.info(f'Closing the current window')
        self.driver.close()
        return self

    def quit(self):
        """
        Quits the driver and closes every associated window.

        :return: self
        """
        log.info(f'Quits the driver and closes every associated window')
        self.driver.quit()
        return self

    def page_back(self):
        """
        Goes one step backward in the browser history.

        :return: self
        """
        log.info(f'Goes one step backward in the browser history')
        self.driver.back()
        return self

    def page_forward(self):
        """
        Goes one step forward in the browser history.

        :return: self
        """
        log.info(f'Goes one step forward in the browser history')
        self.driver.forward()
        return self

    def page_refresh(self):
        """
        Refreshes the current page.

        :return: self
        """
        log.info(f'Refreshes the current page')
        self.driver.refresh()
        return self

    def get_page_title(self):
        """
        Returns the title of the current page.

        :return: page title as a string
        """
        log.info(f'Returns the title of the current page')
        return self.driver.title

    def maximize_window(self):
        """
        Maximizes the current window that the WebDriver is using.

        :return: self
        """
        log.info(f'Maximizes the current window that webdriver is using')
        self.driver.maximize_window()
        return self

    def resize_window(self, width, height):
        """
        Sets the current window width and height.

        :param width: The desired window width in pixels
        :param height: The desired window height in pixels
        :return: self
        """
        log.info(f'Sets current window width to: {width}px and height to: {height}px')
        self.driver.set_window_size(width, height)
        return self

    def execute_js_script(self, js_script, arguments=None):
        """
        Executes a JavaScript script with optional arguments.

        :param js_script: The JavaScript script to execute
        :param arguments: Optional arguments for the script
        :return: self
        """
        log.info(f'Execute JS script: {js_script} with arguments: {arguments}')
        self.driver.execute_script(js_script, arguments)
        return self

    def execute_async_js_script(self, js_script, arguments=None):
        """
        Executes an asynchronous JavaScript script with optional arguments.

        :param js_script: The JavaScript script to execute
        :param arguments: Optional arguments for the script
        :return: self
        """
        log.info(f'Execute async JS script: {js_script} with arguments: {arguments}')
        self.driver.execute_async_script(js_script, arguments)
        return self

    def delete_all_cookies(self):
        """
        Deletes all cookies in the scope of the session.

        :return: self
        """
        log.info(f'Delete all cookies in the scope of the session')
        self.driver.delete_all_cookies()
        return self

    def delete_cookie(self, cookie_to_delete):
        """
        Deletes a specific cookie.

        :param cookie_to_delete: The name of the cookie to delete
        :return: self
        """
        log.info(f'Deleting cookie: {cookie_to_delete}')
        self.driver.delete_cookie(cookie_to_delete)
        return self

    def set_cookie(self, cookie_name: dict):
        """
        Sets a new cookie.

        :param cookie_name: A dictionary containing the cookie name and value
        """
        log.info(f'Setting cookie: {cookie_name}')
        self.driver.add_cookie(cookie_name)

    def get_all_cookies(self):
        """
        Returns a set of dictionaries corresponding to cookies visible in the current session.

        :return: self
        """
        log.info(f'Returns a set of dictionaries, corresponding to cookies visible in the current session')
        self.driver.get_cookies()
        return self

    def get_cookie(self, cookie):
        """
        Gets a single cookie.

        :param cookie: The name of the cookie to retrieve
        :return: self
        """
        log.info(f' Get a single cookie: {cookie}')
        self.driver.get_cookie(cookie)
        return self

    def switch_to_frame(self, frame_id):
        """
        Switches the WebDriver focus to the specified frame.

        :param frame_id: The ID of the frame to switch to
        :return: self
        """
        log.info(f'Switching to frame: {frame_id}')
        self.driver.switch_to.frame(frame_id)
        return self

    def switch_to_default(self):
        """
        Switches the WebDriver focus to the default frame.

        :return: self
        """
        log.info(f'Switching focus to the default frame')
        self.driver.switch_to.default_content()
        return self

    def dismiss_alert(self):
        """
        Dismisses the alert.

        :return: self
        """
        log.info(f'Dismissing the alert')
        self.driver.switch_to.alert.dismiss()
        return self

    def accept_alert(self):
        """
        Accepts the alert.

        :return: self
        """
        log.info(f'Accepting alert')
        self.driver.switch_to.alert.accept()
        return self

    def type_in_alert(self, value):
        """
        Types the specified value in the alert.

        :param value: The value to type in the alert
        :return: self
        """
        log.info(f'Typing in alert: {value}')
        self.driver.switch_to.alert.text(value)
        return self

    def click_with_delay(self, selector, delay=2):
        """
        Clicks on an element only after it becomes visible and adds an additional delay before click.

        :param selector: The element to click on
        :param delay: The additional delay in seconds (default is 2)
        :return: self
        """
        self.waiter.wait_for_element_to_be_visible(selector)
        self.waiter.strict_wait(delay)
        log.info(f'Clicking on element: {selector} with delay: {delay}')
        self.finder.find(selector).click()

    def click(self, selector):
        """
        Clicks on an element after it becomes visible.

        :param selector: The element to click on
        :return: self
        """
        self.waiter.wait_for_element_to_be_visible(selector)
        log.info(f'Clicking on element: {selector}')
        self.finder.find(selector).click()

    def scroll_to(self, selector):
        """
        Scrolls to an element.

        :param selector: The element to scroll to
        :return: self
        """
        target = self.finder.find(selector)
        log.info(f'Scrolling to element: {selector}')
        self.execute_js_script('arguments[0].scrollIntoView({block: "center"})', target)

    def get_text_from_element(self, selector):
        """
        Gets the text from an element after it becomes visible.

        :param selector: The element to get text from
        :return: The text of the element
        """
        self.waiter.wait_for_element_to_be_visible(selector)
        log.info(f'Getting text from element: {selector}')
        return self.finder.find(selector).text

    def fill_field(self, selector, value):
        """
        Fills a field with a specified value after the field becomes visible.

        :param selector: The field to fill
        :param value: The value to fill in the field
        :return: self
        """
        self.waiter.wait_for_element_to_be_visible(selector)
        log.info(f'Filling field: {selector} with value: {value}')
        self.finder.find(selector).send_keys(value)
        return self

    def fill_form(self, selector_data):
        """
        Fills multiple fields in a form using a dictionary of selectors and values.

        :param selector_data: A dictionary of selectors and values
        :return: self
        """
        if type(selector_data) is dict:
            for selector, data in selector_data.items():
                self.waiter.wait_for_element_to_be_visible(selector)
                log.info(f'Filling field: {selector} with value: {data}')
                self.finder.find(selector).send_keys(data)
        return self

    def move_mouse_on_element(self, selector):
        """
        Moves the mouse cursor over an element after the element becomes visible.

        :param selector: The element to move the mouse cursor over
        :return: self
        """
        self.waiter.wait_for_element_to_be_visible(selector)
        element = self.finder.find(selector)
        log.info(f'Moving mouse on element: {selector}')
        ActionChains(self.driver).move_to_element(element)
        return self

    def press_key(self, key):
        """
        Presses a specified key.

        :param key: The key to press
        :return: self
        """
        log.info(f'Pressing key: {key}')
        actions = ActionChains(self.driver)
        actions.send_keys(key).perform()
        return self

    def send_keys(self, selector, keys):
        """
        Sends keys to a specified field.

        :param selector: The field to send keys to
        :param keys: The keys to send
        :return: self
        """
        log.info(f'Send keys: {keys} to the field: {selector}')
        self.finder.find(selector).send_keys(keys)
        return self

    def submit_form(self, selector):
        """
        Submits a form using a specified selector.

        :param selector: The form to submit
        :return: self
        """
        log.info(f'Submitting form: {selector}')
        self.finder.find(selector).submit()
        return self

    def clear_field(self, selector):
        """
        Clears a field after it becomes visible.

        :param selector: The field to clear
        :return: self
        """
        self.waiter.wait_for_element_to_be_visible(selector)
        log.info(f'Clearing field: {selector}')
        self.finder.find(selector).clear()
        return self
