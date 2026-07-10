# Adding Custom Browser Options
This documentation will guide you through the process of adding custom browser options using VigilantDriver and the 
Selenium WebDriver.

## Steps
1. Create an instance of the browser Options class

Use the Options class for the browser you're running:

- Chrome: `selenium.webdriver.chrome.options.Options` or `webdriver.ChromeOptions()`
- Firefox: `selenium.webdriver.firefox.options.Options` or `webdriver.FirefoxOptions()`

```python
from selenium import webdriver

opts = webdriver.ChromeOptions()
```

2. Add your custom arguments and settings
Next, you can add your custom arguments and settings to the Options() instance. These arguments and settings will be 
applied to the browser when it is launched.

For example, let's say you want to run the browser in headless mode (without a visible GUI). You can add the 
headless argument to achieve this (Chrome and Firefox use different flags):

```python
opts.add_argument('--headless')   # Chrome
# opts.add_argument('-headless')  # Firefox
```

Feel free to add any other desired arguments or settings as needed. Refer to the Selenium WebDriver documentation for 
more information on available options.

3. Pass the custom browser options to VigilantDriver

Finally, you need to pass the custom browser options to the VigilantDriver() class, which will create an instance of the
browser with the specified options.

```python
browser = VigilantDriver(browser_options=opts)
```

## Example Usage
Here's an example usage of adding custom browser options using VigilantDriver and the Selenium WebDriver:

```python
import unittest
from vigilant.driver.vigilant_driver import VigilantDriver
from selenium import webdriver

class TestHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        opts = webdriver.FirefoxOptions()
        
        # Add some arguments, in our case to make the browser headless
        opts.add_argument('-headless')                 
        
        # Pass custom browser options to the VigilantDriver() class
        cls.browser = VigilantDriver(browser_options=opts)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()

    def test_home_page(self):
        self.browser.get_page('/')  # Requires BASE_URL to be set
        self.browser.assertions.see_in_title('Python')


if __name__ == '__main__':
    unittest.main()

```

In this example, the browser is set to run in headless mode, and the test navigates to the root page and asserts that 
the page title contains the string 'Python'.

## Conclusion

By following these steps, you can add custom browser options to your Selenium WebDriver tests using VigilantDriver. This
allows you to customize the browser's behavior and tailor it to your specific testing requirements.
