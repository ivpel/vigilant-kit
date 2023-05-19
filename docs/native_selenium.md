# Using Native Selenium Methods
This documentation provides instructions on how to utilize native Selenium WebDriver methods from the `VigilantDriver()`
instance in your test scripts.

## Steps
1. Create an instance of VigilantDriver

```python
act = VigilantDriver()
```
2. Access native Selenium methods
To access native Selenium WebDriver methods, you can utilize the `driver` attribute of the `VigilantDriver()` instance.

```python
act.driver.get('https://python.org') # Will use native Selenium get() method
act.get_page('https://python.org') # Will use native get() method under the hood.
```

## Example Usage
Here's an example that demonstrates the usage of native Selenium methods from the `VigilantDriver()` instance:

```python
import unittest
from vigilant.driver.vigilant_driver import VigilantDriver
from selenium.webdriver.firefox.options import Options


class TestHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.act = VigilantDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.act.quit()

    def test_home_page(self):
        """
        To use native Selenium WebDriver methods - use `driver` attribute

            self.act.drive.get() - method from Selenium WebDriver to access page

            self.act.get_page() - method from VigilantDriver()
        """
        self.act.driver.get('https://python.org')

        self.act.assertions.see_in_title('Python')

if __name__ == '__main__':
    unittest.main()

```
In this example, the `get()` method is used from the driver attribute of the `VigilantDriver()` instance to navigate to
the 'https://python.org' URL. Subsequently, the `assertions.see_in_title()` method is used to verify that the page title 
contains the string 'Python'.

## Conclusion
By following these steps, you can leverage the native Selenium WebDriver methods directly from the `VigilantDriver()` 
instance in your test scripts. This allows you to take advantage of the full capabilities of Selenium while benefiting 
from the additional features provided by `VigilantDriver()`.