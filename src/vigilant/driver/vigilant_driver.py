import os
from src.vigilant.actions.vigilant_actions import VigilantActions
from selenium import webdriver
from src.vigilant.logger import logger as log


class VigilantDriver:
    """
    This class provide methods for running WebDriver client from scratch using configuration
    provided inside .src.env file.
    Environment variables as configuration artifacts that should be inside .src.env file
    SELENIUM_HOST - is used as command_executor, it is Selenium Server URI;
    SELENIUM_BROWSER - used as entity that show which browser options to use FirefoxOptions(),
        ChromeOptions, etc. (DesiredCapabilities is now deprecated, we should use Options() class).
    BASE_URL - the root URL of the application under test
    WAIT_TIMEOUT - configuration for the default amount of time (in seconds) that a
    test will wait while trying to interact with web element.
    LOGGER_LEVEL - level of verbosity that will be printed in to the console;
    """

    def __init__(self):
        """
        In this constructor we initialize two attributes:
        `driver` - native webdriver client, created from .src.env configuration file;
        `act` - instance of VigilantActions class, which is wrapper on native WebDriver methods to interact
        with browser.
        """
        self.driver = self.create_remote_session()
        self.vigilant = VigilantActions(self.driver)

    SELENIUM_HOST = os.environ.get("SELENIUM_HOST")
    SELENIUM_BROWSER = os.environ.get("SELENIUM_BROWSER")

    def default_browser_options(self):
        """
        Set browser options according to browser name provided in .src.env file.
        It can be overwritten when user create new Selenium session by providing options as argument.
        :return:
        """
        options = None
        if self.SELENIUM_BROWSER.lower() == "firefox":
            options = webdriver.FirefoxOptions()
        elif self.SELENIUM_BROWSER.lower() == "chrome":
            options = webdriver.ChromeOptions()
        log.info(f"Setting default browser options: {self.SELENIUM_BROWSER}")
        return options

    def create_remote_session(self, browser_options=None):
        log.info("Creating remote session.\n"
                 f"Command executor: {self.SELENIUM_HOST}\n"
                 f"Browser: {self.SELENIUM_BROWSER}")

        if browser_options is None:
            browser_options = self.default_browser_options()

        return webdriver.Remote(command_executor=self.SELENIUM_HOST,
                                options=browser_options)
