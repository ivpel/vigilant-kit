# Vigilant Kit
Minimal Selenium helpers that stay out of your way. Use any test runner (pytest, unittest, behave, raw scripts), keep full WebDriver control, and get convenience actions/assertions without a framework telling you how to structure tests.

## Why Vigilant?
* **Minimal & composable**: Thin wrapper over Selenium; mix our helpers with native WebDriver any time.
* **Framework-agnostic**: Works with pytest, unittest, behave, custom runners, or plain scripts.
* **Quick wins**: Smart waits, handy finders, assertions, PDF helpers, and data savers ready to use.
* **Customizable**: Bring your own browser options, config via env or YAML, extend actions/assertions as needed.
* **Standards-based**: Built on Selenium WebDriver (W3C).

## Quick start

Install Vigilant Kit and make sure Chrome is available on your machine. Selenium Manager will resolve the matching
driver automatically.

```shell
pip install vigilant-kit
```

Create `smoke_test.py`:

```python
from vigilant.driver import Config
from vigilant.driver.vigilant_driver import VigilantDriver


config = Config(
    selenium_browser="chrome",
    selenium_host="local",
    base_url="https://example.com",
)

browser = VigilantDriver(config=config)
try:
    browser.get_page("/")
    browser.assertions.see_in_title("Example Domain")
    print(browser.get_page_title())
finally:
    browser.quit()
```

Run it as a regular Python script:

```shell
python smoke_test.py
```

The browser opens `https://example.com`, verifies its title, prints `Example Domain`, and closes even if the assertion
fails. The same `VigilantDriver` object can be used from pytest, unittest, behave, or another runner.

## What's included?
_Wait, Act, Assert_


### **Actions** 
   - `click()`
   - `scroll_to()`
   - `fill_form()`
   - `switch_to_window()`
   - ...

### **Waiters for condition** 

   - `wait_for_element_to_be_visible()`
   - `wait_for_element_to_be_clickable()`
   - `wait_for_text_to_be_present_in_element()`
   - `wait_for_element_to_disappear()`
   - ...

### **Assertions** 

   - `see_element()`
   - `dont_see()`
   - `see_text()`
   - `see_in_title()`
   - ...




### **Scrappers**
Minimal required methods for scraping some data:
  - `get_text_from_element()`
  - `get_attribute_from_element()`
  - `get_cookie()`
  - `save_data_to_txt()`

### **Test PDF**
You're testing some eCommerce project, and you need to check your PDF invoice file? No problem!
   - `find_pdf_file()`,
   - `assert_strings_in_pdf()`,
   - `assert_strings_not_in_pdf()`,
   - `find_file_and_assert_strings_are_in()`,
   - ...

And much more! Check list of all available - [Actions](docs/actions.md)


## Extending Functionality
If you need something that is not covered in this library, you still have access to all native `Selenium WebDriver` 
methods. You can create your own methods or use native `WebDriver` methods and share them on one browser session.

## Install
```shell
pip install vigilant-kit
```

Python 3.10 or newer is required.

Configuration can be supplied through environment variables or an instance-scoped typed object:

```python
from vigilant.driver.config import Config
from vigilant.driver.vigilant_driver import VigilantDriver

browser = VigilantDriver(config=Config.from_yaml("vgl.yaml"))
```

## Docs

### Configuration
- [Vigilant configuration](docs/configuration.md)
- [Adding custom browser options](docs/browser_options.md)
- [Using native selenium methods](docs/native_selenium.md)
- [BiDi helpers (console/network)](docs/bidi.md)

### Examples & tutorials
- [Quick start example using `unittest` library](docs/vigilant_unittest.md) 
- [Quick start example using `pytest`](docs/vigilant_pytest.md) 
- [Testing ecommerce project using `vigilant-kit` and `pytest`](docs/tutorial_pytest.md)

### Actions
- [List of actions](docs/actions.md)

## Development

Run the unit suite without starting a browser:

```shell
PYTHONPATH=src python -m unittest discover -s tests -v
```
