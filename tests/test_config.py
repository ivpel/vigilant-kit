import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from vigilant.driver import load_config_from_yaml
from vigilant.driver.config import Config, VigilantConfig


class ConfigTests(unittest.TestCase):
    def test_alias_is_public_config_class(self):
        self.assertIs(Config, VigilantConfig)

    def test_from_env_converts_timeout(self):
        config = Config.from_env(
            {
                "SELENIUM_BROWSER": "firefox",
                "SELENIUM_HOST": "local",
                "BASE_URL": "https://example.com",
                "WAIT_TIMEOUT": "2.5",
                "LOGGER_LEVEL": "DEBUG",
            }
        )

        self.assertEqual(config.selenium_browser, "firefox")
        self.assertEqual(config.wait_timeout, 2.5)
        self.assertEqual(config.logger_level, "DEBUG")

    def test_from_env_rejects_invalid_timeout(self):
        with self.assertRaisesRegex(ValueError, "could not convert string to float"):
            Config.from_env({"WAIT_TIMEOUT": "soon"})

    def test_from_yaml_reads_vgl_section(self):
        path = self._yaml(
            "vgl:\n"
            "  SELENIUM_BROWSER: chrome\n"
            "  BASE_URL: https://example.com\n"
            "  WAIT_TIMEOUT: 7\n"
        )

        config = Config.from_yaml(path)

        self.assertEqual(config.selenium_browser, "chrome")
        self.assertEqual(config.base_url, "https://example.com")
        self.assertEqual(config.wait_timeout, 7.0)

    def test_from_yaml_returns_empty_config_when_optional_file_is_missing(self):
        self.assertEqual(Config.from_yaml("does-not-exist.yaml"), Config())

    def test_from_yaml_can_raise_when_file_is_missing(self):
        with self.assertRaises(FileNotFoundError):
            Config.from_yaml("does-not-exist.yaml", raise_on_missing=True)

    def test_from_yaml_rejects_invalid_section(self):
        path = self._yaml("vgl:\n  - chrome\n")

        with self.assertRaisesRegex(ValueError, "to be a mapping"):
            Config.from_yaml(path)

    def test_from_yaml_reports_invalid_timeout_with_context(self):
        path = self._yaml("vgl:\n  WAIT_TIMEOUT: later\n")

        with self.assertRaisesRegex(ValueError, "WAIT_TIMEOUT.*must be numeric"):
            Config.from_yaml(path)

    def test_merge_prefers_non_none_values_from_other(self):
        environment = Config(selenium_browser="firefox", base_url="https://old", wait_timeout=5)
        explicit = Config(selenium_browser="chrome", base_url="", logger_level="DEBUG")

        merged = environment.merged(explicit)

        self.assertEqual(merged.selenium_browser, "chrome")
        self.assertEqual(merged.base_url, "")
        self.assertEqual(merged.wait_timeout, 5)
        self.assertEqual(merged.logger_level, "DEBUG")

    def test_apply_to_env_honours_overwrite_flag(self):
        with patch.dict(os.environ, {"SELENIUM_BROWSER": "firefox"}, clear=True):
            Config(selenium_browser="chrome", wait_timeout=3).apply_to_env(overwrite=False)
            self.assertEqual(os.environ["SELENIUM_BROWSER"], "firefox")
            self.assertEqual(os.environ["WAIT_TIMEOUT"], "3")

    def test_legacy_loader_applies_yaml_to_environment(self):
        path = self._yaml("vgl:\n  SELENIUM_BROWSER: chrome\n")
        with patch.dict(os.environ, {}, clear=True):
            self.assertTrue(load_config_from_yaml(path))
            self.assertEqual(os.environ["SELENIUM_BROWSER"], "chrome")

    @staticmethod
    def _yaml(contents: str) -> str:
        handle, path = tempfile.mkstemp(suffix=".yaml")
        os.close(handle)
        Path(path).write_text(contents, encoding="utf-8")
        return path


if __name__ == "__main__":
    unittest.main()
