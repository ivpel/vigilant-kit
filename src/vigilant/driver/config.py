from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

import os
import yaml


@dataclass(frozen=True)
class VigilantConfig:
    """
    Typed configuration for Vigilant Kit.

    Precedence (highest to lowest) is typically:
    explicit arguments > VigilantConfig > environment variables.
    """

    selenium_browser: str | None = None
    selenium_host: str | None = None
    base_url: str | None = None
    wait_timeout: float | None = None
    logger_level: str | None = None

    @staticmethod
    def _coerce_float(value: Any) -> float:
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, str):
            return float(value.strip())
        raise TypeError(f"Expected numeric value, got {type(value).__name__}")

    @classmethod
    def from_env(cls, env: Mapping[str, str] | None = None) -> "VigilantConfig":
        env = os.environ if env is None else env

        raw_timeout = env.get("WAIT_TIMEOUT")
        wait_timeout = None
        if raw_timeout not in (None, ""):
            wait_timeout = cls._coerce_float(raw_timeout)

        return cls(
            selenium_browser=env.get("SELENIUM_BROWSER") or None,
            selenium_host=env.get("SELENIUM_HOST") or None,
            base_url=env.get("BASE_URL") or None,
            wait_timeout=wait_timeout,
            logger_level=env.get("LOGGER_LEVEL") or None,
        )

    @classmethod
    def from_yaml(
        cls,
        yaml_path: str = "vgl.yaml",
        *,
        raise_on_missing: bool = False,
        root_key: str = "vgl",
    ) -> "VigilantConfig":
        path = Path(yaml_path)
        if not path.exists():
            if raise_on_missing:
                raise FileNotFoundError(f"Could not find `{yaml_path}` configuration file.")
            return cls()

        with path.open("r", encoding="utf-8") as file:
            configs = yaml.safe_load(file) or {}

        if not isinstance(configs, dict):
            raise ValueError(f"Expected YAML document in `{yaml_path}` to be a mapping")

        section = configs.get(root_key, {})
        if not isinstance(section, dict):
            raise ValueError(f"Expected `{root_key}` in `{yaml_path}` to be a mapping")

        wait_timeout = section.get("WAIT_TIMEOUT")
        coerced_timeout = None
        if wait_timeout not in (None, ""):
            try:
                coerced_timeout = cls._coerce_float(wait_timeout)
            except (TypeError, ValueError) as exc:
                raise ValueError(f"WAIT_TIMEOUT in `{yaml_path}` must be numeric, got: {wait_timeout!r}") from exc

        def _get(key: str) -> str | None:
            value = section.get(key)
            if value in (None, ""):
                return None
            return str(value)

        return cls(
            selenium_browser=_get("SELENIUM_BROWSER"),
            selenium_host=_get("SELENIUM_HOST"),
            base_url=_get("BASE_URL"),
            wait_timeout=coerced_timeout,
            logger_level=_get("LOGGER_LEVEL"),
        )

    def merged(self, other: "VigilantConfig") -> "VigilantConfig":
        """
        Merge two configs, preferring values from `other` when they are not None.
        """
        return VigilantConfig(
            selenium_browser=other.selenium_browser if other.selenium_browser is not None else self.selenium_browser,
            selenium_host=other.selenium_host if other.selenium_host is not None else self.selenium_host,
            base_url=other.base_url if other.base_url is not None else self.base_url,
            wait_timeout=other.wait_timeout if other.wait_timeout is not None else self.wait_timeout,
            logger_level=other.logger_level if other.logger_level is not None else self.logger_level,
        )

    def apply_to_env(self, *, overwrite: bool = True) -> None:
        """
        Populate `os.environ` from this config.

        :param overwrite: if False, only sets keys that are not already present.
        """

        def _set(key: str, value: Any) -> None:
            if value is None:
                return
            if not overwrite and os.environ.get(key) not in (None, ""):
                return
            os.environ[key] = str(value)

        _set("SELENIUM_BROWSER", self.selenium_browser)
        _set("SELENIUM_HOST", self.selenium_host)
        _set("BASE_URL", self.base_url)
        _set("WAIT_TIMEOUT", self.wait_timeout)
        _set("LOGGER_LEVEL", self.logger_level)


# Convenience alias for public API.
Config = VigilantConfig
