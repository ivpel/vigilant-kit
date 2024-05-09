# Changelog for Vigilant Kit

### [Logic behind Changelog](docs/changelog_logic.md)

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



