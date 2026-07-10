# Vigilant Configuration

Vigilant Kit reads configuration from environment variables. Optionally, you can load them from a YAML file (`vgl.yaml`)
via `vigilant.driver.load_config_from_yaml()`.

You can also use a typed config object, which avoids relying on global process environment:

```python
from vigilant.driver.config import Config
from vigilant.driver.vigilant_driver import VigilantDriver

cfg = Config.from_yaml()  # reads ./vgl.yaml if present
browser = VigilantDriver(config=cfg)
```

Values are resolved in this order (highest precedence first): explicit `VigilantDriver` constructor arguments, the
typed config object, then environment variables. Passing a typed config does not modify `os.environ`.

## Configuration Options

Vigilant can be configured with the following options:

**BASE_URL**

- **Description**: The base URL of the website to be tested.
- **YAML Path**: `vgl.BASE_URL`
- **Example**: `BASE_URL: http://www.python.org`

**SELENIUM_HOST**

- **Description**: The Selenium server host URL, or `local` to use a local browser.
- **YAML Path**: `vgl.SELENIUM_HOST`
- **Example**: `SELENIUM_HOST: local` or `SELENIUM_HOST: http://127.0.0.1:4444/wd/hub`

When you use `SELENIUM_HOST: local` (recommended for local development), Vigilant creates a local WebDriver session.

**SELENIUM_BROWSER**

- **Description**: The browser to be used for testing.
- **YAML Path**: `vgl.SELENIUM_BROWSER`
- **Example**: `SELENIUM_BROWSER: firefox`

**WAIT_TIMEOUT**

- **Description**: The timeout duration (in seconds) for wait operations.
- **YAML Path**: `vgl.WAIT_TIMEOUT`
- **Example**: `WAIT_TIMEOUT: 10`

**LOGGER_LEVEL**

- **Description**: The logging level for Vigilant.
- **YAML Path**: `vgl.LOGGER_LEVEL`
- **Example**: `LOGGER_LEVEL: INFO`

## Configuration File

Create a `vgl.yaml` file (see `vgl.yaml.example` in the repo) with this structure:

```yaml
vgl:
  BASE_URL: http://www.python.org
  SELENIUM_HOST: local # or http://127.0.0.1:4444/wd/hub for remote Selenium/Grid
  SELENIUM_BROWSER: firefox
  WAIT_TIMEOUT: 10
  LOGGER_LEVEL: INFO
```

## Environment Variables
For backward compatibility, YAML can instead be loaded into environment variables once early in your test suite:

```python
from vigilant.driver import load_config_from_yaml

load_config_from_yaml()  # defaults to ./vgl.yaml (no error if missing)
```

Or, export variables directly in your shell/CI:

```shell
export SELENIUM_HOST=local SELENIUM_BROWSER=chrome BASE_URL=https://example.com WAIT_TIMEOUT=10 LOGGER_LEVEL=INFO
```
