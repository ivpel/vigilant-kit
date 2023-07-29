# Changelog for Vigilant Kit

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



