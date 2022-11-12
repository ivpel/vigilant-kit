# How to add custom browser options

Let's use example from Quick Start section.
Adding custom browser options can be done in 3 steps:
1. Create instance of Options() class
2. Add your custom arguments and did anything you want.
3. Pass that options in to VigilantDriver()

```python
import unittest

from vigilant.driver.vigilant_driver import VigilantDriver
from selenium.webdriver.firefox.options import Options


class TestHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # Create instance of Options() class
        opts = Options()                    
        
        # Add some arguments, in our case to make browser headless
        opts.add_argument('-headless')                 
        
        # Pass custom browser options to the VigilantDriver() class
        cls.act = VigilantDriver(browser_options=opts) 

    @classmethod
    def tearDownClass(cls) -> None:
        cls.act.quit()

    def test_home_page(self):
        # Case 1. Go to some page and assert page title
        self.act.get_page('/')  # Go to root page
        self.act.assertions.see_in_title('Python')  # Assert that page title contains 'Python' string


if __name__ == '__main__':
    unittest.main()

```