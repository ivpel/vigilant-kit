## Quick start
We will write our first test with `unittest` library. Also make sure that you installed
`vigilant-kit` library.


### Configuration
Configuration can be done through environment variables, or via `vgl.yaml` loaded at runtime. If you want to run against
a remote Selenium server/Grid, see: [Selenium setup](selenium_install.md)

Example `vgl.yaml`:
```yaml
vgl:
  SELENIUM_HOST: local
  SELENIUM_BROWSER: firefox
  BASE_URL: http://www.python.org
  WAIT_TIMEOUT: 10
  LOGGER_LEVEL: INFO
```

Alternatively, you can avoid YAML-to-env loading and pass a typed config object:
```python
from vigilant.driver.config import Config
from vigilant.driver.vigilant_driver import VigilantDriver

browser = VigilantDriver(config=Config.from_yaml())
```

### Test
Create file `test_first.py` with same code as below. We will cover 3 simple cases for demo purposes.
```python
import unittest

from vigilant.driver import load_config_from_yaml
from vigilant.driver.vigilant_driver import VigilantDriver


class TestHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        load_config_from_yaml()  # reads ./vgl.yaml if present (safe to call even if missing)
        cls.act = VigilantDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.act.quit()

    def test_home_page(self):
        # Case 1. Go to some page and assert page title
        self.act.get_page('/')  # Go to root page
        self.act.assertions.see_in_title('Python')  # Assert that page title contains 'Python' string

    def test_text_block(self):
        # Case 2. Scroll to some block and assert visible text
        self.act.get_page('/')  # Go to root page
        self.act.scroll_to('//h2[text()="Success Stories"]')  # Scroll to Success Stories block
        self.act.assertions.see_text('Success Stories')  # Assert that Success Stories string is visible

    def test_search_page(self):
        # Case 3. Fill in Search field with search key word, assert result in search result page.
        self.act.get_page('/')  # Go to root page
        self.act.fill_field('//input[@name="q"]', 'python')  # Fill search field
        self.act.click('//button[@id="submit"]')  # Click Search button
        self.act.assertions.see_in_url(
            '/search/?q=python')  # See in URL that we are redirected to search result page
        self.act.assertions.see_text('Results')  # Assert visible Results text


if __name__ == '__main__':
    unittest.main()

```
Now run our script:
```shell
python3 test_first.py
```
### Results
If you are running your Selenium Server locally - you can see how script interact with browser in real time. But in any
case you should have terminal output similar to this, due to LOGGER_LEVEL=INFO:
```text
[2022-11-02 16:34:26,452: INFO] Creating remote session.
Command executor: http://127.0.0.1:4444/wd/hub
Browser: firefox
[2022-11-02 16:34:26,452: INFO] Setting default browser options: firefox
[2022-11-02 16:34:27,890: INFO] Getting page: /
[2022-11-02 16:34:33,942: INFO] Assert: see string Python in current page title
[2022-11-02 16:34:33,956: INFO] Scrolling to element: //h2[text()="Success Stories"]
[2022-11-02 16:34:33,956: INFO] Execute JS script: arguments[0].scrollIntoView({block: "center"}) with arguments: <selenium.webdriver.remote.webelement.WebElement (session="3c63a627-1ffd-40ed-b008-78e671d82085", element="703e049a-3ab4-4bd5-814a-bb38dd64864a")>
[2022-11-02 16:34:33,980: INFO] Waiting for element with selector: //input[@name="q"] - to be visible.
[2022-11-02 16:34:33,991: INFO] Filling field: //input[@name="q"] with value: python
[2022-11-02 16:34:34,012: INFO] Waiting for element with selector: //button[@id="submit"] - to be visible.
[2022-11-02 16:34:34,026: INFO] Clicking on element: //button[@id="submit"]
[2022-11-02 16:34:34,411: INFO] Assert: see string /search/?q=python in current page URL
[2022-11-02 16:34:34,434: INFO] Quits the driver and closes every associated window

```
Congrats! You successfully created your first testing script using Vigilant Kit :)
