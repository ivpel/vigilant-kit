# Changelog for Vigilant Kit

### [Logic behind Changelog](docs/changelog_logic.md)

## Version 1.7.1

### Fixes & improvements
- Added GitHub Actions CI for Python 3.10–3.13 and package build validation.
- Added automated GitHub Actions dependency updates through Dependabot.
- Added a CI status badge to the README.
- Corrected repository, documentation, and issue tracker links in package metadata.

## Version 1.7.0

### New features
- Added immutable typed configuration via `vigilant.driver.config.Config`.
- `VigilantDriver(config=...)` now resolves settings with the precedence: explicit constructor arguments, typed config, environment variables.
- Added `Config.from_env()`, `Config.from_yaml()`, `Config.merged()`, and the backward-compatible `apply_to_env()` helper.

### Fixes & improvements
- Instance configuration now supplies `BASE_URL`, waiter timeouts, and logger level without mutating process environment.
- YAML configuration reports malformed documents, invalid `vgl` sections, and invalid `WAIT_TIMEOUT` values with contextual errors.
- Relative navigation now normalizes slashes between `BASE_URL` and the requested path.
- JavaScript helpers now expand argument sequences as Selenium expects.
- Updated and simplified configuration, Selenium setup, actions, pytest, and unittest documentation.
- Added unit coverage for configuration precedence, YAML loading, local/remote driver creation, URL handling, logging, and JavaScript arguments.

### Compatibility
- Minimum supported Python version is now 3.10, matching the type syntax used by the package.
- `load_config_from_yaml()` retains its environment-based behavior for backward compatibility.

## Version 1.6.0

### New features
- Added optional BiDi-based assertions: `no_console_errors()` and `no_js_errors()`.
- Added optional BiDi-based waiter helpers: `wait_for_response()` and `wait_for_network_idle()`.
- BiDi features skip (with a warning) when BiDi/DevTools websocket is not available (common on cloud/Grid providers).
- Added documentation: `docs/bidi.md`.

## Version 1.5.1

### Fixes & improvements
- Added safe default/validation for `WAIT_TIMEOUT`; clarified waiter log messages.
- Fixed alert typing (`send_keys`), hover execution (`perform`), and restored method chaining/returns for click/scroll/tab/window helpers.
- Cookie getters now return data instead of `self`; BASE_URL guard added for `get_page`.
- Expanded XPath detection to selectors starting with `(`.
- Swapped import-time config side effects for an explicit `load_config_from_yaml`; switched prints to logger in config loader and data saver.

## Version 1.5.0

### Code refactor
- Name of core configuration file was changed, from `vgl_config.yaml` to `vgl.yaml`
- Methods for interacting with URLs have been renamed to more fully reflect what they actually do.
  - `get_page()` - now used for navigation through paths relative to BASE_URL
  - `go_to()` - opens the page by the URL without relation to any configuration.

## Version 1.4.6

### Code refactor
- Fixed `VigilantDriver()` class to accept custom browser options, browser type, and host settings during instantiation.
- Modified `VigilantDriver.__init__()` to accept optional parameters for browser_options, selenium_browser, and selenium_host.
- Updated methods `default_browser_options()` and `create_driver_session()` to accommodate new initialization parameters.

## Version 1.4.5

### Code refactor 

- Refactored class `VigilantDriver()`, refactored methods for creating driver sessions, added docstrings.

## Version 1.4.4

### Code refactor & New features

- Added new class that allows to test PDF files `VigilantPDF`
- Added new method `find_pdf_file()` - find PDF files that match a given regex pattern within the specified directory.
- Added new method `assert_strings_are_in_file()` - assert that all strings in the list are found in the specified PDF files.
- Added new method `assert_strings_are_not_in_file()` - assert that none of the strings in the list are found in the specified PDF files.
- Added new method `assert_strings_in_pdf()` - check if all strings in the list are present in the specified PDF file.
- Added new method `assert_strings_not_in_pdf()` - check if none of the strings in the list are present in the specified PDF file.
- Added new method `delete_pdf_file()` - find and delete all PDF files that follow the specified regex pattern.
- Added new method `find_file_and_assert_strings_are_in()` - find PDF files and ensure the specified strings are present in each.
- Added new method `find_file_and_assert_strings_are_not_in()` - find PDF files and ensure the specified strings are not present in any of them.

### Dependencies

- Removed pacakge: `python-dotenv`.
- Removed pacakge: `requests`.
- Removed pacakge: `psutil`.

## Version 1.4.3

### Code refactor & New methods

- Refactor `by_xpath_or_css()` - so it can detect positional selectors.
- Added new method `save_data_to_txt()` - can be used to write different data in to .txt file.


## Version 1.4.2

### Code refactor & New methods

- Refactor `click()` - wait until visible, scroll and then click.
- Added new action `instant_click()` - click on element without any conditions.
- Added new action `scroll_to_the_to_of_page()` - scrolling to the top of the page.
- Added new assertion `see_text_in_dom()` - assert that text is presented in the DOM tree.
- Added doc with description of logic behind the CHANGELOG file.


## Version 1.4.1

### Code Refactoring
- Split methods for accessing pages: `get_relative_page()` (if **BASE_URL** is used) and 
`get_page()` if **BASE_URL** is not used.


## Version 1.4.0

### Code Refactoring
- Removed `vgl` CLI.
- Updated `VigilantDriver` class, now scripts can be run without Selenium server, only using local browser.
- Updated documentation related to new configuration.

### Dependencies

- Removed pacakge: `click`.


## Version 1.3.0

### New Features

- Changed way of configuration for local development. Introduced `vgl_config.yaml` file.
- Updated documentation related to new configuration.

### Dependencies

- Added new dependency: `pyyaml`.

## Version 1.2.9

### Code Refactoring

- Refactor `vgl` CLI so it more simple and clear now.

## Version 1.2.8

### New Features

- Introduced CHANGELOG.md to keep track of project changes.
- Implemented `selenium` command group, providing the following commands:
  - `run`: Starts the Selenium server.
  - `stop`: Stops the Selenium server.
  - Various options are now available for the Selenium commands.
  - Added the ability to stop the Selenium server as a daemon in a single command.
  - For more information and usage details, run `vgl selenium --help`.

### Dependencies

- Added new dependency: `psutils`.

### Code Refactoring

- Improved styles for error messages in `assertions.py`.
