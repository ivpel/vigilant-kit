from __future__ import annotations

from dataclasses import is_dataclass, asdict
from contextlib import AsyncExitStack
from typing import Any, Callable, Optional

import trio
from selenium.common.exceptions import WebDriverException

from vigilant.logger import logger as log


def _warn_bidi_unavailable_once(driver: Any, exc: BaseException) -> None:
    """
    Emit a single warning per driver instance when BiDi/CDP socket access
    cannot be established.
    """
    flag = "_vigilant_bidi_unavailable_warned"
    if getattr(driver, flag, False):
        return
    setattr(driver, flag, True)
    log.warning(
        "BiDi is not available for this session (skipping). "
        "This is common on cloud/Grid providers because the DevTools/BiDi websocket "
        "endpoint (debuggerAddress / se:cdp) is not exposed or not reachable from the client. "
        "Original error: %s",
        exc,
    )


def _trio_run(async_fn: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """
    Run a Trio async function from sync code.
    """
    return trio.run(async_fn, *args, **kwargs)


def _remote_object_to_str(obj: Any) -> str:
    for key in ("value", "description", "unserializable_value"):
        value = getattr(obj, key, None)
        if value is not None:
            return str(value)
    try:
        if is_dataclass(obj):
            return str(asdict(obj))
    except Exception:
        pass
    return str(obj)


def _extract_console_text(event: Any) -> str:
    args = getattr(event, "args", None) or []
    if not args:
        return ""
    return " ".join(_remote_object_to_str(a) for a in args)


def _extract_exception_text(event: Any) -> str:
    details = getattr(event, "exception_details", None)
    if details is None:
        return str(event)
    text = getattr(details, "text", None) or ""
    exception_obj = getattr(details, "exception", None)
    if exception_obj is not None:
        desc = getattr(exception_obj, "description", None) or getattr(exception_obj, "value", None)
        if desc:
            return f"{text} {desc}".strip()
    return text or str(details)


class VigilantBiDi:
    """
    Adapter around Selenium's `driver.bidi_connection()` with explicit failure policy.
    """

    def __init__(self, driver: Any):
        self._driver = driver

    def supported(self) -> bool:
        return hasattr(self._driver, "bidi_connection")

    def run(
        self, async_fn: Callable[..., Any], *args: Any,
        on_unavailable: str = "raise", **kwargs: Any
    ) -> Optional[Any]:
        """
        Run an async function that receives a `BidiConnection` as its first argument.
        Connection failures raise BiDiUnavailableError by default. Opt into
        on_unavailable="warn" to log and return None instead. Operation errors,
        including timeouts, always propagate.
        """
        if on_unavailable not in ("raise", "warn"):
            raise ValueError('on_unavailable must be "raise" or "warn"')

        def unavailable(exc: BaseException) -> None:
            if on_unavailable == "raise":
                raise BiDiUnavailableError("BiDi/CDP connection is unavailable") from exc
            _warn_bidi_unavailable_once(self._driver, exc)

        if not self.supported():
            return unavailable(RuntimeError("driver has no bidi_connection()"))

        async def _runner() -> Any:
            async with AsyncExitStack() as stack:
                try:
                    bidi = await stack.enter_async_context(self._driver.bidi_connection())
                except (WebDriverException, OSError) as exc:
                    return unavailable(exc)
                return await async_fn(bidi, *args, **kwargs)

        return _trio_run(_runner)


class BiDiUnavailableError(RuntimeError):
    """The requested BiDi/CDP check could not establish a connection."""
