# Changelog for Vigilant Kit
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



