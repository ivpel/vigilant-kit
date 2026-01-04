# BiDi helpers (Chrome/Firefox notes)

Vigilant Kit is a thin wrapper around Selenium, but it also provides a few **optional** helpers that use Selenium 4's
`bidi_connection()` API to observe browser **console**, **JavaScript exceptions**, and **network activity**.

These helpers are best-effort:
- On local runs, they often work in Chrome (and may work in Firefox depending on driver support).
- On cloud/Grid providers, they are frequently **unavailable** because the DevTools/BiDi websocket endpoint is not
  exposed or not reachable from the client. In that case Vigilant logs a warning and **skips** the BiDi-based wait/assert.

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

## Tips
- Call BiDi-based waiters/assertions close to the action that triggers the event you care about.
- For deterministic UI state, prefer classic Selenium explicit waits (`wait_for_element_*`) where possible.

