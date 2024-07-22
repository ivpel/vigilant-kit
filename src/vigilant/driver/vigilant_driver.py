import os
from selenium import webdriver
from vigilant.actions.vigilant_actions import VigilantActions
from vigilant.logger import logger as log

class VigilantDriver(VigilantActions):
    """
    Custom web driver for automated browser interactions.

    Attributes:
        SELENIUM_HOST (str): The host for Selenium (local or remote).
        SELENIUM_BROWSER (str): The browser to use (e.g., 'firefox', 'chrome').

    Methods:
        default_browser_options: Returns the default browser options based on the SELENIUM_BROWSER.
        create_driver_session: Creates a Selenium driver session (local or remote).
    """

    def __init__(self, browser_options=None, selenium_browser=None, selenium_host=None):
        """
        Initializes the VigilantDriver with the specified browser and host settings.
        Raises a ValueError if SELENIUM_BROWSER is not set or if the specified browser is unsupported.
        """
        self.SELENIUM_BROWSER = selenium_browser or os.environ.get("SELENIUM_BROWSER")
        self.SELENIUM_HOST = selenium_host or os.environ.get("SELENIUM_HOST")

        if not self.SELENIUM_BROWSER:
            raise ValueError("SELENIUM_BROWSER environment variable is not set")

        if browser_options is None:
            browser_options = self.default_browser_options()

        if self.SELENIUM_HOST in ["local", None, ""]:
            self.driver = self.create_driver_session(browser_options)
        else:
            self.driver = self.create_driver_session(browser_options, remote=True)
        super().__init__(self.driver)

    def default_browser_options(self):
        """
        Returns the default browser options based on the SELENIUM_BROWSER environment variable.

        Raises:
            ValueError: If SELENIUM_BROWSER is not set or the specified browser is unsupported.

        Returns:
            options (webdriver.Options): The options for the specified browser.
        """
        if not self.SELENIUM_BROWSER:
            raise ValueError("SELENIUM_BROWSER is not set")

        options = None
        browser = self.SELENIUM_BROWSER.lower()
        if browser == "firefox":
            options = webdriver.FirefoxOptions()
        elif browser == "chrome":
            options = webdriver.ChromeOptions()
        else:
            raise ValueError(f"Unsupported browser: {self.SELENIUM_BROWSER}")

        log.info(f"Setting default browser options: {self.SELENIUM_BROWSER}")
        return options

    def create_driver_session(self, browser_options, remote=False):
        """
        Creates a Selenium driver session.

        Args:
            browser_options (webdriver.Options): The browser options to use for the session.
            remote (bool): Flag indicating whether to create a remote session. Default is False.

        Raises:
            ValueError: If the specified browser is unsupported.

        Returns:
            webdriver.WebDriver: The Selenium WebDriver instance.
        """
        if remote:
            log.info("Creating remote session.\n"
                     f"Command executor: {self.SELENIUM_HOST}\n"
                     f"Browser: {self.SELENIUM_BROWSER}")
            return webdriver.Remote(command_executor=self.SELENIUM_HOST,
                                    options=browser_options)
        else:
            log.info("Creating local session.\n"
                     f"Browser: {self.SELENIUM_BROWSER}")
            if self.SELENIUM_BROWSER.lower() == "firefox":
                return webdriver.Firefox(options=browser_options)
            elif self.SELENIUM_BROWSER.lower() == "chrome":
                return webdriver.Chrome(options=browser_options)
            else:
                raise ValueError(f"Unsupported browser: {self.SELENIUM_BROWSER}")
