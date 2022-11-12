# How to use native Selenium methods

How to use native webdriver methods from `VigilantDriver()` instance?

Example:
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
