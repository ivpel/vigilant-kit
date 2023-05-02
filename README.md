# Vigilant Kit
Vigilant is a set of tools designed to help write and run robust functional tests using Selenium WebDriver. It provides
methods for interacting with the WebBrowser, assertions, and waiting. With Vigilant, you can start writing complex test
cases in a minute and configure the process easily with just one .vigilant.env file.

## Why Vigilant?
- **Easy to start**: One `.vigilant.env` file for configuration, one `vgl install dev-kit` script for installing
Selenium Standalone Server and Webdriver for browser.
- **Flexible Framework Usage**: Usage is not limited to a single testing framework; you can use Vigilant with unittest,
  pytest, or anything else.
- **Faster Test Writing**: Vigilant provides you with methods that help you write functional tests quickly without
  spending time on writing boilerplate code every time you start a new project.

## What it includes?
Methods for **interacting** with WebBrowser (`click`, `scroll_to`,  etc.), **assertions** (`see`, `dont_see`, `see_text`
, etc.) **waiting** (`wait_for_element_to_be_visible`, `wait_for_element_to_be_clickable`, etc.)
It is already there, ready to use.

Also, a bunch of CLI scripts, to make your life easier!

Use `vgl --help` to see all available commands.

List of all available [actions](docs/actions.md).

## Extending Functionality
If you need something that is not covered in this library, you still have access to all native `Selenium WebDriver` 
methods. You can create your own methods or use native `WebDriver` methods and share them on one browser session.

## Install
```shell
pip install vigilant-kit
```

## Docs
 - [How to install Selenium server & browser drivers](docs/selenium_install.md)
 - [Quick start example using `unittest` library](docs/vigilant_unittest.md) 
 - [Quick start example using `pytest`](docs/vigilant_pytest.md) 
 - [How to add custom browser options](docs/browser_options.md)
 - [Access native Selenium WebDriver methods](docs/native_selenium.md)
 - [List of actions](docs/actions.md).

## Tutorials
 - [Testing ecommerce project using `vigilant-kit` and `pytest`](docs/tutorial_pytest.md)
 