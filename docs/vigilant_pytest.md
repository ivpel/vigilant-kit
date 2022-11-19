# How to start testing with `pytest`

If you are not familiar with `pytest` - there is good place to start:
[Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)

Official `pytest` documentation is pretty good as well: 
[pytest](https://docs.pytest.org/en/latest/index.html)

Example using `pytest`
```python
import pytest

from vigilant.driver.vigilant_driver import VigilantDriver


@pytest.fixture()
def act():
    act = VigilantDriver()
    yield act
    act.quit()


def test_homepage(act):
    # Case 1. Go to some page and assert page title
    act.get_page('/')  # Go to root page
    act.assertions.see_in_title('Python')  # Assert that page title contains 'Python' string


def test_stories(act):
    # Case 2. Scroll to some block and assert visible text
    act.get_page('/') # Go to root page
    act.scroll_to('//h2[text()="Success Stories"]')  # Scroll to Success Stories block
    act.assertions.see_text('Success Stories')  # Assert that Success Stories string is visible


def test_search_page(act):
    # Case 3. Fill in Search field with search key word, assert result in search result page.
    act.get_page('/') # Go to root page
    act.fill_field('//input[@name="q"]', 'python')  # Fill search field
    act.click('//button[@id="submit"]')  # Click Search button
    act.assertions.see_in_url(
        '/search/?q=python')  # See in URL that we are redirected to search result page
    act.assertions.see_text('Results')  # Assert visible Results text


```

How to use fixture similar to `setUpClass` from `unittest`?
Use `scope` argument for fixture:
```text
    :param scope:
        The scope for which this fixture is shared; one of ``"function"``
        (default), ``"class"``, ``"module"``, ``"package"`` or ``"session"``.
```
This fixture will be shared for all tests on scope of module without reinitializing it (similar to `setUpBeforeClass`).
```python
import pytest

from vigilant.driver.vigilant_driver import VigilantDriver


@pytest.fixture(scope="module")
def act():
    act = VigilantDriver()
    yield act
    act.quit()


def test_homepage(act):
    # Case 1. Go to some page and assert page title
    act.get_page('/')  # Go to root page
    act.assertions.see_in_title('Python')  # Assert that page title contains 'Python' string


def test_stories(act):
    # Case 2. Scroll to some block and assert visible text
    act.scroll_to('//h2[text()="Success Stories"]')  # Scroll to Success Stories block
    act.assertions.see_text('Success Stories')  # Assert that Success Stories string is visible

```