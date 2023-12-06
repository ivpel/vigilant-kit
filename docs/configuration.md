# Vigilant Configuration

Vigilant is a Selenium-based library that allows you to automate web testing tasks. The configuration of Vigilant is 
available through simple `vgl_config.yaml` file.

## Configuration Options

Vigilant can be configured with the following options:

**BASE_URL**

- Description: The base URL of the website to be tested.
- YAML Path: selenium-configuration.BASE_URL
- Example: BASE_URL: http://www.python.org

**SELENIUM_HOST**

- Description: The Selenium server host URL.
- YAML Path: selenium-configuration.SELENIUM_HOST
- Example: SELENIUM_HOST: http://127.0.0.1:4444/wd/hub

**SELENIUM_BROWSER**

- Description: The browser to be used for testing.
- YAML Path: selenium-configuration.SELENIUM_BROWSER
- Example: SELENIUM_BROWSER: firefox

**WAIT_TIMEOUT**

- Description: The timeout duration (in seconds) for wait operations.
- YAML Path: selenium-configuration.WAIT_TIMEOUT
- Example: WAIT_TIMEOUT: 10

**LOGGER_LEVEL**

- Description: The logging level for Vigilant.
- YAML Path: selenium-configuration.LOGGER_LEVEL
- Example: LOGGER_LEVEL: INFO

## Configuration File

The configuration file `vgl_config.yaml` should be structured as follows:

```yaml
selenium-configuration:
  BASE_URL: http://www.python.org
  SELENIUM_HOST: http://127.0.0.1:4444/wd/hub
  SELENIUM_BROWSER: firefox
  WAIT_TIMEOUT: 10
  LOGGER_LEVEL: INFO
test-credentials:
  file: {credentials_file_name}.yaml
```
You can modify the values in the YAML file to suit your specific configuration requirements.

## Test Credentials
For secure storage of sensitive information like credentials, the YAML configuration file supports referencing an external file:
```yaml
test-credentials:
  file: {credentials_file_name}.yaml
```
Ensure that credentials.yaml is properly secured and not checked into version control.

## Environment Variables
Vigilant will automatically load these settings as environment variables at runtime. There's no need to manually set 
environment variables if they are defined in the `vgl_config.yaml` file.