import logging
import os
import unittest
from unittest.mock import MagicMock, patch

from vigilant.driver.config import Config
from vigilant.driver.vigilant_driver import VigilantDriver
from vigilant.logger import logger


class VigilantDriverTests(unittest.TestCase):
    def setUp(self):
        self.previous_log_level = logger.level

    def tearDown(self):
        logger.setLevel(self.previous_log_level)

    @patch("vigilant.driver.vigilant_driver.webdriver.Chrome")
    def test_config_creates_local_driver_without_mutating_environment(self, chrome):
        chrome.return_value = MagicMock()
        config = Config(
            selenium_browser="chrome",
            selenium_host="local",
            base_url="https://example.com/",
            wait_timeout=4,
        )

        with patch.dict(os.environ, {}, clear=True):
            driver = VigilantDriver(config=config)
            self.assertNotIn("SELENIUM_BROWSER", os.environ)
            self.assertNotIn("BASE_URL", os.environ)

        chrome.assert_called_once()
        self.assertEqual(driver.waiter.timeout, 4)
        self.assertEqual(driver.assertions.waiter.timeout, 4)

    @patch("vigilant.driver.vigilant_driver.webdriver.Chrome")
    def test_explicit_arguments_override_config_and_environment(self, chrome):
        chrome.return_value = MagicMock()
        with patch.dict(
            os.environ,
            {"SELENIUM_BROWSER": "firefox", "SELENIUM_HOST": "https://grid.invalid"},
            clear=True,
        ):
            driver = VigilantDriver(
                selenium_browser="chrome",
                selenium_host="local",
                config=Config(selenium_browser="firefox"),
            )

        self.assertEqual(driver.SELENIUM_BROWSER, "chrome")
        self.assertEqual(driver.SELENIUM_HOST, "local")
        chrome.assert_called_once()

    @patch("vigilant.driver.vigilant_driver.webdriver.Remote")
    def test_remote_config_creates_remote_driver(self, remote):
        remote.return_value = MagicMock()
        driver = VigilantDriver(
            config=Config(selenium_browser="chrome", selenium_host="https://grid.example/wd/hub")
        )

        self.assertIs(driver.driver, remote.return_value)
        remote.assert_called_once()
        self.assertEqual(remote.call_args.kwargs["command_executor"], "https://grid.example/wd/hub")

    @patch("vigilant.driver.vigilant_driver.webdriver.Chrome")
    def test_config_sets_logger_level(self, chrome):
        chrome.return_value = MagicMock()
        VigilantDriver(config=Config(selenium_browser="chrome", logger_level="DEBUG"))
        self.assertEqual(logger.level, logging.DEBUG)

    @patch("vigilant.driver.vigilant_driver.webdriver.Chrome")
    def test_get_page_uses_instance_base_url_and_normalizes_slashes(self, chrome):
        native_driver = MagicMock()
        chrome.return_value = native_driver
        driver = VigilantDriver(
            config=Config(selenium_browser="chrome", base_url="https://example.com/root/")
        )

        driver.get_page("/login")

        native_driver.get.assert_called_once_with("https://example.com/root/login")

    @patch("vigilant.driver.vigilant_driver.webdriver.Chrome")
    def test_execute_script_expands_argument_sequence(self, chrome):
        native_driver = MagicMock()
        chrome.return_value = native_driver
        driver = VigilantDriver(config=Config(selenium_browser="chrome"))

        driver.execute_js_script("return arguments", ["one", "two"])

        native_driver.execute_script.assert_called_once_with("return arguments", "one", "two")

    def test_rejects_wrong_config_type(self):
        with self.assertRaisesRegex(TypeError, "VigilantConfig"):
            VigilantDriver(config={"SELENIUM_BROWSER": "chrome"})


if __name__ == "__main__":
    unittest.main()
