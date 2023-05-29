# Vigilant Kit
Vigilant is a set of tools designed to help write and run robust functional tests using Selenium WebDriver. With 
Vigilant, you can start writing complex test cases in a minute.

## Why Vigilant?
* **Easy to start & Fast To Write**: Vigilant provides you with methods that help you write functional tests quickly 
without spending time on writing boilerplate code every time you start a new project.
* **Flexible Framework Usage**: Usage is not limited to a single testing framework; you can use Vigilant with unittest,
  pytest, or anything else.
* **Stability**: We use Selenium WebDriver. It is a W3C Recommendation.
   - WebDriver drives a browser natively, as a user would, either locally or on a remote machine using the Selenium server.
   - WebDriver is designed as a simple and more concise programming interface.
   - WebDriver is a compact object-oriented API.
   - It drives the browser effectively.

## What it includes?
Vigilant include methods for interacting with browser,  for asserting conditions and also methods for waiting 
those conditions.

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


Also, CLI scripts included, to make your life easier!

Use `vgl --help` to see all available commands.


## Extending Functionality
If you need something that is not covered in this library, you still have access to all native `Selenium WebDriver` 
methods. You can create your own methods or use native `WebDriver` methods and share them on one browser session.

## Install
```shell
pip install vigilant-kit
```

## Docs
### Install
- [How to install Selenium server & browser drivers](docs/selenium_install.md)

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
