# Vigilant Kit
Minimal Selenium helpers that stay out of your way. Use any test runner (pytest, unittest, behave, raw scripts), keep full WebDriver control, and get convenience actions/assertions without a framework telling you how to structure tests.

## Why Vigilant?
* **Minimal & composable**: Thin wrapper over Selenium; mix our helpers with native WebDriver any time.
* **Framework-agnostic**: Works with pytest, unittest, behave, custom runners, or plain scripts.
* **Quick wins**: Smart waits, handy finders, assertions, PDF helpers, and data savers ready to use.
* **Customizable**: Bring your own browser options, config via env or YAML, extend actions/assertions as needed.
* **Standards-based**: Built on Selenium WebDriver (W3C).

## Quick start
```shell
pip install vigilant-kit
export SELENIUM_BROWSER=chrome SELENIUM_HOST=local BASE_URL=https://example.com
```

```python
from vigilant.driver.vigilant_driver import VigilantDriver

def test_login():
    browser = VigilantDriver()
    browser.get_page("/login") \
           .fill_form({"#email": "user@example.com", "#password": "secret"}) \
           .click("#submit")
    browser.assertions.see_text("Welcome")
    browser.quit()
```
Use your runner of choice: pytest, unittest, behave, or a simple Python script.

## What included?
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

   - `see()`
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
