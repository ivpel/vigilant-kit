# Vigilant Kit
Vigilant is a set of tools designed to help write and run robust functional tests using Selenium WebDriver. With 
Vigilant, you can start writing complex test cases in a minute.

## Why Vigilant?
* **Easy to start & Fast To Write**: Vigilant provides you with methods that help you write functional tests quickly 
without spending time on writing boilerplate code every time you start a new project.
* **No limit in usage**: You are not limited to a single testing framework; you can use Vigilant with **unittest**,
  **pytest**, or for **scrapping data**. It's just a tool, use it as you want.
* **Stability**: We use Selenium WebDriver. It is a **W3C standard**.
   - WebDriver drives a browser natively, as a user would, either locally or on a remote machine using the Selenium server.
   - WebDriver is designed as a simple and more concise programming interface.
   - WebDriver is a compact object-oriented API.
   - It drives the browser effectively.

## What it includes?
Vigilant provide a suite of methods designed for efficient browser interaction, robust assertion of various 
conditions, and adaptive waiting mechanisms to accommodate different states and conditions.

**Interacting with WebBrowser** 
   - `click()`
   - `scroll_to()`
   - `fill_form()`
   - `move_mouse_on_element()`
   - ...

**Assertions** 
   - `see()`
   - `dont_see()`
   - `see_text()`
   - `see_in_title()`
   - ...


**Waiters** 
   - `wait_for_element_to_be_visible()`
   - `wait_for_element_to_be_clickable()`
   - `wait_for_text_to_be_present_in_element()`
   - `wait_for_element_to_disappear()`
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

### Examples & tutorials
- [Quick start example using `unittest` library](docs/vigilant_unittest.md) 
- [Quick start example using `pytest`](docs/vigilant_pytest.md) 
- [Testing ecommerce project using `vigilant-kit` and `pytest`](docs/tutorial_pytest.md)

### Actions
- [List of actions](docs/actions.md)
