# Vigilant Kit
**Vigilant** is a set of tools designed to help write and run robust functional tests using Selenium WebDriver. With 
**Vigilant**, you can start writing complex test cases in a minute.

## Why Vigilant?
* **Easy to start & Fast To Write**: All methods for interaction, waiting different conditions and asserting the results
are already here.
* **No limits**: You are not limited to a single testing framework, use Vigilant with **unittest**,
  **pytest**, or for **scrapping data**. 
* **Stability**: We use Selenium WebDriver. It is a **W3C standard**.


## What included?
_Wait for condition, Act by Interaction, Assert the result._


### **Actions** 
   - `click()` - click on element when it visible and scrolled in to the view;
   - `scroll_to()` - easy scroll to the element when necessary;
   - `fill_form()` - fill form with many fields without repetitive;
   - `switch_to_window()` - work with multiply browser windows without any issues;
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
Minimal required methods for scrapping some data:
  - `get_text_from_element()`
  - `get_attribute_from_element()`
  - `get_cookie()`
  - `save_data_to_txt()`

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

### Examples & tutorials
- [Quick start example using `unittest` library](docs/vigilant_unittest.md) 
- [Quick start example using `pytest`](docs/vigilant_pytest.md) 
- [Testing ecommerce project using `vigilant-kit` and `pytest`](docs/tutorial_pytest.md)

### Actions
- [List of actions](docs/actions.md)
