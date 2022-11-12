# How to start testing with `unittest` library

If you are not already familiar with the basic concepts of testing, you might want to read this tutorial:
[unittest](https://docs.python.org/3/library/unittest.html)

Example using `unittest` library.
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

