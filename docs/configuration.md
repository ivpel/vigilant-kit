# Vigilant Configuration

Vigilant is a Selenium-based library that allows you to automate web testing tasks. The configuration of Vigilant can be
customized using environment variables. You have the option to configure Vigilant using either a `.vigilant.env` file or
a `vigilant.json` file. Alternatively, you can directly set the configuration using environment variables of your choice.

## Configuration Options
**BASE_URL**

    Description: The base URL of the website to be tested.
    Environment Variable: BASE_URL
    Example: BASE_URL=http://www.python.org

**SELENIUM_HOST**

    Description: The Selenium server host URL.
    Environment Variable: SELENIUM_HOST
    Example: SELENIUM_HOST=http://127.0.0.1:4444/wd/hub

**SELENIUM_BROWSER**

    Description: The browser to be used for testing.
    Environment Variable: SELENIUM_BROWSER
    Example: SELENIUM_BROWSER=firefox

**WAIT_TIMEOUT**

    Description: The timeout duration (in seconds) for wait operations.
    Environment Variable: WAIT_TIMEOUT
    Example: WAIT_TIMEOUT=10

**LOGGER_LEVEL**

    Description: The logging level for Vigilant.
    Environment Variable: LOGGER_LEVEL
    Example: LOGGER_LEVEL=INFO

## Configuration Files
**vigilant.json**

The `vigilant.json` file allows you to define the configuration options in a JSON format. Here's an example of the 
`vigilant.json` file:
```json
{
  "BASE_URL": "http://www.python.org",
  "SELENIUM_HOST": "http://127.0.0.1:4444/wd/hub",
  "SELENIUM_BROWSER": "firefox",
  "WAIT_TIMEOUT": 10,
  "LOGGER_LEVEL": "INFO"
}
```

You can modify the values in the JSON file to suit your specific configuration requirements.
`.vigilant.env`

The `.vigilant.env` file allows you to define the configuration options in a key-value format. Each configuration option
is set as an environment variable. Here's an example of the `.vigilant.env` file:
```shell
BASE_URL=http://www.python.org
SELENIUM_HOST=http://127.0.0.1:4444/wd/hub
SELENIUM_BROWSER=firefox
WAIT_TIMEOUT=10
LOGGER_LEVEL=INFO

```
Each line represents a configuration option in the format **KEY=VALUE**.

## Environment Variables

Alternatively, you can directly set the configuration options using environment variables of your choice. Simply set the desired environment variables with the appropriate values.

## Note

Ensure that you have the required dependencies and tools installed for Vigilant, such as Selenium and the corresponding browser drivers.

By configuring Vigilant using the methods mentioned above, you can customize its behavior to suit your testing needs and automate web testing tasks effectively.