# BiDi helpers (Chrome/Firefox notes)

Vigilant Kit is a thin wrapper around Selenium, but it also provides a few **optional** helpers that use Selenium 4's
`bidi_connection()` API to observe browser **console**, **JavaScript exceptions**, and **network activity**.

These helpers use Selenium's DevTools/CDP session through `bidi_connection()`; they are not a native W3C BiDi
implementation. Availability depends on the browser, Selenium version, and access to the websocket endpoint.

By default, a missing connection API or a WebDriver/OS error while establishing the connection raises
`vigilant.bidi.BiDiUnavailableError`. To explicitly allow unavailable checks to return without validation, pass
`on_unavailable="warn"`. This logs one warning per driver; it does not mark a test as skipped in your test runner.
Timeouts, errors during an established session, and unexpected implementation errors always propagate, including
when the warning policy is selected.

## Assertions

```python
browser.assertions.no_console_errors(observe_seconds=1.0)
browser.assertions.no_js_errors(observe_seconds=1.0)
```

Both methods observe for a short window and fail if errors appear during that time.

## Waiter

```python
browser.waiter.wait_for_response(url_contains="/api/login", status=200, timeout=10)
browser.waiter.wait_for_network_idle(idle_ms=500, timeout=10)
```

To preserve the previous best-effort behavior for unavailable connections:

```python
browser.assertions.no_console_errors(on_unavailable="warn")
browser.waiter.wait_for_response(url_contains="/api/login", on_unavailable="warn")
```

The same option is available on `no_js_errors()` and `wait_for_network_idle()`.

## Tips
- Helpers observe events after their listeners are registered; they do not replay earlier responses or errors.
- Network idle tracks requests observed during the call; requests already in flight before subscription are not included.
- For deterministic UI state, prefer classic Selenium explicit waits (`wait_for_element_*`) where possible.
