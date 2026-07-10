# Actions, waiters, assertions

Vigilant Kit is a thin wrapper over Selenium WebDriver. You keep full access to the underlying driver via
`VigilantDriver.driver`, while getting a few convenience helpers for common patterns.

## Core object model

```python
from vigilant.driver.vigilant_driver import VigilantDriver

browser = VigilantDriver()
```

`VigilantDriver` exposes:
- **Direct actions** on the driver (for example `get_page()`, `go_to()`, `click()`, `fill_field()`, `scroll_to()`, etc.)
- **Helpers** via attributes:
  - `browser.waiter` – explicit waits around elements and (optionally) BiDi network waits
  - `browser.assertions` – small assertions over page state and (optionally) BiDi error checks
  - `browser.finder` – element lookup helpers (CSS/XPath convenience)
  - `browser.vgl_pdf` – PDF assertions/helpers

## Navigation

- `browser.get_page("/path")` uses `BASE_URL` and navigates to `BASE_URL + "/path"`.
- `browser.go_to("https://example.com")` navigates to an absolute URL.

## Waiter

Element waits (WebDriverWait):
- `wait_for_element_to_be_visible(selector)`
- `wait_for_element_to_be_clickable(selector)`
- `wait_for_element_to_be_present_in_dom(selector)`
- `wait_for_element_to_disappear(selector)`
- `wait_for_text_to_be_present_in_element(selector, text)`
- `wait_for_text_to_be_present_in_element_value(selector, value_text)`
- `wait_for_text_to_be_present_in_element_attribute(selector, text_in_attribute)`
- `wait_for_alert_()`

BiDi-based waits (best-effort; skip with a warning when unavailable, common on cloud/Grid):
- `wait_for_response(url_contains=..., url_equals=..., status=..., timeout=...)`
- `wait_for_network_idle(idle_ms=..., timeout=...)`

## Assertions

Common assertions:
- `see_element(selector|list)`
- `dont_see(selector|list)`
- `see_in_title(text)` / `dont_see_in_title(text)`
- `see_in_url(text)` / `dont_see_in_current_url(text)`
- `see_text(text)` / `see_text_in_dom(text)`

BiDi-based assertions (best-effort; skip with a warning when unavailable, common on cloud/Grid):
- `no_console_errors(observe_seconds=...)`
- `no_js_errors(observe_seconds=...)`

## “Native Selenium”

Everything Selenium can do is still available:

```python
browser.driver.execute_script("console.log('hi')")
browser.driver.get("https://example.com")
```

See also: [Using native selenium methods](native_selenium.md).

