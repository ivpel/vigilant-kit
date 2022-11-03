import os

from selenium import webdriver

from vigilant.actions.vigilant_actions import VigilantActions
from vigilant.logger import logger as log


class VigilantDriver:
    """
    VigilantDriver class provide methods for running WebDriver client from scratch using configuration
    from .vigilant.env file.

    Environment variables are configuration items that should be inside .vigilant.env file:
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
        `driver` - native webdriver client, created from .vigilant.env configuration file;
        `vigilant` - instance of VigilantActions class, which is wrapper on native WebDriver methods to interact
        with browser.
        """
        self.driver = self.create_remote_driver_session()
        self.vigilant = VigilantActions(self.driver)

    SELENIUM_HOST = os.environ.get("SELENIUM_HOST")
    SELENIUM_BROWSER = os.environ.get("SELENIUM_BROWSER")

    def default_browser_options(self):
        """
        Set browser options according to browser name provided in .vigilant.env file.
        It can be overwritten when user create new Selenium session by providing options as argument.

        Returns:
            Options: return default browser options according to value from SELENIUM_BROWSER variable.
        """
        options = None
        if self.SELENIUM_BROWSER.lower() == "firefox":
            options = webdriver.FirefoxOptions()
        elif self.SELENIUM_BROWSER.lower() == "chrome":
            options = webdriver.ChromeOptions()
        log.info(f"Setting default browser options: {self.SELENIUM_BROWSER}")
        return options

    def create_remote_driver_session(self, browser_options=None):
        """
        Create a new driver that will issue commands using the wire protocol.

         Args:
            browser_options: browser options instance is required as it determines which browser will be used

        Returns:
            Remote: remote driver session based on configuration from .vigilant.env file
        """
        log.info("Creating remote session.\n"
                 f"Command executor: {self.SELENIUM_HOST}\n"
                 f"Browser: {self.SELENIUM_BROWSER}")

        if browser_options is None:
            browser_options = self.default_browser_options()

        return webdriver.Remote(command_executor=self.SELENIUM_HOST,
                                options=browser_options)
