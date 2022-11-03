# Vigilant Kit
Vigilant is a set of tools made to help writing and running robust functional tests using Selenium WebDriver. 

## Why Vigilant?
 - It allows you to start writing complex test cases in a minute.
 - Simple configuration process (just one `.vigilant.env` file to start)
 - Usage is not limited to a single testing framework, it can be used with `unittest`, `pytest` or anything else.
It is up to you.

## Flexibility 
**Vigilant** provide you with methods that help write functional tests fast, without spending your time on writing smart
waiters, finders and assertions. Methods for interacting with WebBrowser (`click`, `scroll_to`, etc.), assertions 
(`see`, `dont_see`, `see_text`, etc.) It is already there, ready to use.

What if you need something that is not covered in this library?

You still have access to all `WebDriver` methods. Despite all functional that library provide - you can create your own 
methods or use native `WebDriver` methods.

Check documentation to find more.

## Docs & Tutorials
If you are interested how to use **Vigilant Kit** with such framework as `unittest` or `pytest` with complex cases, POM 
pattern, etc. - visit documentation part.

If you just want to see what is **Vigilant Kit** and what it can do - **Quick start** is good place to start.

## Quick start
We will write our first test without any classic test frameworks, it will be simple python script, but it enough
to show how easy it can be to start. If you want to start with `unittest` or `pytest` check our documentation with
tutorials and examples.
### Install
```shell
pip install vigilant-kit
```

### Configuration
Configuration can be done through environment variables. Create `.vigilant.env` file with next data:
```shell
# Selenium host URL
SELENIUM_HOST=http://127.0.0.1:4444/wd/hub 

# Browser which will performing the tests
SELENIUM_BROWSER=firefox 

# The root URL of the application under test.
BASE_URL=http://www.python.org 

# Amount of time (in seconds) that a test will wait while loading a page or waiting for element
WAIT_TIMEOUT=10 

# Log level
LOGGER_LEVEL=INFO 
```

### Test
Create file `first_test.py` with same code as below. We will cover 3 simple cases for demo purposes.
```python
from vigilant.driver.vigilant_driver import VigilantDriver


def first_test():
    driver = VigilantDriver() # Creating Browser session

    # Case 1. Go to some page and assert page title
    driver.vigilant.get_page('/') # Go to root page
    driver.vigilant.assertions.see_in_title('Python') # Assert that page title contains 'Python' string
    
    # Case 2. Scroll to some block and assert visible text
    driver.vigilant.scroll_to('//h2[text()="Success Stories"]') # Scroll to Success Stories block
    driver.vigilant.assertions.see_text('Success Stories') # Assert that Success Stories string is visible 

    # Case 3. Fill in Search field with search key word, assert result in search result page.
    driver.vigilant.fill_field('//input[@name="q"]', 'python') # Fill search field
    driver.vigilant.click('//button[@id="submit"]') # Click Search button
    driver.vigilant.assertions.see_in_url('/search/?q=python') # See in URL that we are redirected to search result page
    driver.vigilant.assertions.see_text('Results') # Assert visible Results text

    driver.vigilant.quit() # Quit browser session


if __name__ == '__main__':
    first_test()

```
Now run our script:
```shell
python3 first_test.py
```
### Results
If you are running your selenium server locally - you can see how script interact with browser in real time. But in any
case you should have terminal output similar to this, due to LOGGER_LEVEL=INFO:
```shell
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
