# Testing ecommerce project
In this tutorial, we will learn how to use `vigilant-kit` with `pytest` in real-like project
with **POM** pattern and **fixtures**.

This is a simplified example, but it is enough to understand how it works and be able to apply and use it on your project!

Good luck!

Source code: [vigilant-kit and pytest](https://github.com/ivpel/vigilant-pytest)

Pytest docs: [pytest](https://docs.pytest.org/en/latest/getting-started.html)

## Table of content:
1. [Install `pytest`, `vigilant-kit` and `Selenium Webdriver` server.](#installation-part)
2. [POM pattern.](#pom-pattern)
3. [Writing tests.](#writing-tests)

## Installation part
To install `vigilant-kit` in your project, run this command:
```shell
pip install vigilant-kit
```
Then we need to install `pytest`:
```shell
pip install pytest
```
How to install and run Selenium Server described here [Install Selenium Server](https://github.com/ivpel/vigilant-kit/blob/main/docs/selenium_install.md)

## POM pattern
What is POM pattern?
Page Object Model (POM) is a design pattern, popularly used in test automation that creates Object Repository for web UI
elements. The advantage of the model is that it reduces code duplication and improves test maintenance.
Under this model, for each web page in the application, there should be a corresponding Page Class. This Page class will
identify the WebElements of that web page and also contains Page methods which perform operations on those WebElements.

For our basic ecommerce project we want to have next POM objects:
   1. Login Page
   2. Category List page
   3. Product Page
   4. Cart Page
   5. Checkout Page

## Writing tests
Our test target will be this project: https://www.saucedemo.com/
It is simple, yet perfect for our purposes' resource.

### Tests & dirs structure
Directory - separation between tests type is a good way to manage your tests.
Functional in `functional/` directory, unit tests inside `unit/` directory, etc.

Inside `functional/` dir we need to create two more dirs: 
`fixtures/` - for our fixtures.
`pom/` - for our Page Objects Model objects.

Like this:
```shell
  tests/functional 
    - fixtures/
    - pom/
    - test_name.py
```

Also, don't forget about our configuration file `.vigilant.env`. You can place it in root of your project,
or as example - inside `tests/functional/` directory. 

Example of `.vigilant.env` configuration:
```text
SELENIUM_HOST=http://127.0.0.1:4444/wd/hub
SELENIUM_BROWSER=firefox
BASE_URL=https://www.saucedemo.com
WAIT_TIMEOUT=10
LOGGER_LEVEL=INFO
```

### POM objects
I like to start testing from deciding and describing my Page Objects. So when I will write
actual tests I will already use correct locators from correct Object Repository.
So for which pages we will create POM objects? Check below:
   1. Login Page
   2. Category List page
   3. Product Page
   4. Cart Page
   5. Checkout Page
   

Let's start with Login Page, but first we need to do something else - create BasePage object.
BasePage class will be parent class for all other pages.

`functional/pom/base_page.py`
```python
from vigilant.driver.vigilant_driver import VigilantDriver


class BasePage:

    def __init__(self, driver):
        self.driver: VigilantDriver = driver

```

Using `BasePage` class let's create `LoginPage`.

1. Login page

`functional/pom/login_page.py`
```python
from .base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = '//input[@id="user-name"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//input[@id="login-button"]'

    USERNAME_DATA = 'standard_user'
    PASSWORD_DATA = 'secret_sauce'

    def __init__(self, driver):
        super().__init__(driver)

    def fill_in_and_login(self):
        self.driver.fill_field(self.USERNAME_INPUT, self.USERNAME_DATA)
        self.driver.fill_field(self.PASSWORD_INPUT, self.PASSWORD_DATA)
        self.driver.click(self.LOGIN_BUTTON)
```

2. Category List page

`functional/pom/category_list_page.py`
```python
from .base_page import BasePage


class CategoryListPage(BasePage):

    PRODUCT_CARD = '//div[@class="inventory_item"]'
    PRODUCT_NAME = '//div[@class="inventory_item_name"]'
    ADD_TO_CART_BUTTON = '//button[text()="Add to cart"]'
    PRODUCT_PRICE = '//div[@class="inventory_item_price"]'

    def __init__(self, driver):
        super().__init__(driver)
```

3. Product Detail page

`functional/pom/product_detail_page.py`
```python
from .base_page import BasePage


class ProductDetailPage(BasePage):

    PRODUCT_PRICE = '//div[@class="inventory_details_price"]'
    ADD_TO_CART_BUTTON = '//button[text()="Add to cart"]'
    BACK_TO_CLP_BUTTON = '//button[@id="back-to-products"]'
    
    def __init__(self, driver):
        super().__init__(driver)
```

4. Cart page

`functional/pom/cart_page.py`
```python
from .base_page import BasePage


class CartPage(BasePage):
    
    CART_ICON_LINK = '//a[@class="shopping_cart_link"]'
    PRODUCT_PRICE = '//div[@class="inventory_item_price"]'
    PRODUCT_NAME = '//div[@class="inventory_item_name"]'
    REMOVE_PRODUCT = '//button[text()="Remove"]'
    CONTINUE_SHOPPING_BUTTON = '//button[@id="continue-shopping"]'
    CHECKOUT_BUTTON = '//button[@id="checkout"]'
    
    
    def __init__(self, driver):
        super().__init__(driver)
```

5. Checkout page

`functional/pom/cart_page.py`
```python
from .base_page import BasePage


class CheckoutPage(BasePage):

    # First step checkout
    FIRST_NAME = '//input[@id="first-name"]'
    LAST_NAME = '//input[@id="last-name"]'
    ZIP_CODE = '//input[@id="postal-code"]'
    CONTINUE_BUTTON = '//input[@id="continue"]'
    
    # Second step checkout
    FINISH_BUTTON = '//button[@id="finish"]'
    CANCEL_BUTTON = '//button[@id="cancel"]'
    
    # Checkout complete
    BACK_HOME_BUTTON = '//button[@id="back-to-products"]'
    
    def __init__(self, driver):
        super().__init__(driver)
```

Now let's create Login test.
`functional/test_ecommerce.py`
```python
import pytest

from vigilant.driver.vigilant_driver import VigilantDriver
from pom.login_page import LoginPage


@pytest.fixture(scope="module")
def driver():
    vd = VigilantDriver()
    yield vd
    vd.quit()


def test_login(driver):
    login_page = LoginPage(driver)
    driver.get_page('/')
    login_page.fill_in_and_login()

```
Run it:
```shell
pytest tests/functional/test_ecommerce.py
```

In the example above, we use data from `LoginPage` class, which allow us to use elements locators and
method for login in. So if we will have more tests in the future which require login functionality - we will use
`LoginPage` object, and if something in the project will change - we will need to refactor it only in one place, not in 
the all tests that were affected by changes.

Good! We are now logged in. Go next to the Category List Page and make sure that we can add projects from CLP.

`functional/test_ecommerce.py`
```python
...
from pom.category_list_page import CategoryListPage

...

def test_add_product_from_clp(driver):
    clp = CategoryListPage(driver)

    driver.assertions.see(clp.PRODUCT_CARD + '[1]') # +[1] is Xpath trick to say that we looking for FIRST available element with this selector
    driver.click(clp.ADD_TO_CART_BUTTON + '[1]')
    driver.assertions.see_text('Remove')

```
Great. Now let's add one more tests to check if customer is able to complete order. It will be more complicated test 
if compare to previous one, but also it will show how to use different object in one tests:
`functional/test_ecommerce.py`
```python
...
from pom.cart_page import CartPage
from pom.checkout_page import CheckoutPage

...

def test_complete_order(driver):
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Go to cart page and assert correct url
    driver.click(cart.CART_ICON_LINK)
    driver.assertions.see_in_url('/cart.html')

    # From cart page go to checkout and complete it
    driver.click(cart.CHECKOUT_BUTTON)
    driver.assertions.see_in_url('/checkout-step-one.html')

    # Fill personal info and go to Second step
    checkout.fill_personal_info()
    driver.click(checkout.CONTINUE_BUTTON)
    driver.assertions.see_in_url('checkout-step-two.html')

    # Place order
    driver.click(checkout.FINISH_BUTTON)
    driver.assertions.see_in_url('/checkout-complete.html')

```

Full result:
```python
import pytest

from vigilant.driver.vigilant_driver import VigilantDriver
from pom.login_page import LoginPage
from pom.category_list_page import CategoryListPage
from pom.cart_page import CartPage
from pom.checkout_page import CheckoutPage


@pytest.fixture(scope="module")
def driver():
    vd = VigilantDriver()
    yield vd
    vd.quit()


def test_login(driver):
    login_page = LoginPage(driver)

    driver.get_page('/')
    login_page.fill_in_and_login()
    driver.assertions.see_in_url('/inventory.html')


def test_add_product_from_clp(driver):
    clp = CategoryListPage(driver)

    driver.assertions.see(
        clp.PRODUCT_CARD + '[1]')  # +[1] is Xpath trick to say that we looking for FIRST available element with this selector
    driver.click(clp.ADD_TO_CART_BUTTON + '[1]')
    driver.assertions.see_text('Remove')


def test_complete_order(driver):
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Go to cart page and assert correct url
    driver.click(cart.CART_ICON_LINK)
    driver.assertions.see_in_url('/cart.html')

    # From cart page go to checkout and complete it
    driver.click(cart.CHECKOUT_BUTTON)
    driver.assertions.see_in_url('/checkout-step-one.html')

    # Fill personal info and go to Second step
    checkout.fill_personal_info()
    driver.click(checkout.CONTINUE_BUTTON)
    driver.assertions.see_in_url('checkout-step-two.html')

    # Place order
    driver.click(checkout.FINISH_BUTTON)
    driver.assertions.see_in_url('/checkout-complete.html')

```
Let's run it:
```shell
pytest tests/functional/test_ecommerce.py
```
Result should be this:
```text
==================================================== test session starts ============================================
platform linux -- Python 3.10.6, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/ivan/projects/vigilant_lab
collected 3 items                                                                                                                                                                                                                         

tests/functional/test_ecommerce.py ...                                                                                                                                                                                              [100%]

===================================================== 3 passed in 3.62s =============================================
```

Great! Everything work as expected.

What's next?

As example, you can try to move fixture that setup our browser, in to the `fixture/` directory:
```python
@pytest.fixture(scope="module")
def driver():
    vd = VigilantDriver()
    yield vd
    vd.quit()
```
