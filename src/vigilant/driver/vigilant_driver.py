import os

from selenium import webdriver

from vigilant.actions.vigilant_actions import VigilantActions
from vigilant.logger import logger as log


class VigilantDriver(VigilantActions):

    SELENIUM_HOST = os.environ.get("SELENIUM_HOST")
    SELENIUM_BROWSER = os.environ.get("SELENIUM_BROWSER")

    def __init__(self):
        browser_options = self.default_browser_options()
        if self.SELENIUM_HOST in ["local", None, ""]:
            self.driver = self.create_local_driver_session(browser_options)
        else:
            self.driver = self.create_remote_driver_session(browser_options)
        VigilantActions.__init__(self, self.driver)

    def default_browser_options(self):
        options = None
        if self.SELENIUM_BROWSER.lower() == "firefox":
            options = webdriver.FirefoxOptions()
        elif self.SELENIUM_BROWSER.lower() == "chrome":
            options = webdriver.ChromeOptions()
        log.info(f"Setting default browser options: {self.SELENIUM_BROWSER}")
        return options

    def create_remote_driver_session(self, browser_options):
        log.info("Creating remote session.\n"
                 f"Command executor: {self.SELENIUM_HOST}\n"
                 f"Browser: {self.SELENIUM_BROWSER}")
        return webdriver.Remote(command_executor=self.SELENIUM_HOST,
                                options=browser_options)

    def create_local_driver_session(self, browser_options):
        log.info("Creating local session.\n"
                 f"Browser: {self.SELENIUM_BROWSER}")
        if self.SELENIUM_BROWSER.lower() == "firefox":
            return webdriver.Firefox(options=browser_options)
        elif self.SELENIUM_BROWSER.lower() == "chrome":
            return webdriver.Chrome(options=browser_options)
        raise ValueError("Unsupported browser specified")
