# Actions

# Table of Contents

- [accept_alert(self)](#accept_alertself)
- [by_xpath_or_css(self, selector: str)](#by_xpath_or_cssselfselector:str)
- [clear_field(self, selector)](#clear_fieldselfselector)
- [click(self, selector)](#clickselfselector)
- [click_with_delay(self, selector, delay=2)](#click_with_delayselfselectordelay=2)
- [close(self)](#closeself)
- [count_elements(self, selector: str)](#count_elementsselfselector:str)
- [delete_all_cookies(self)](#delete_all_cookiesself)
- [delete_cookie(self, cookie_to_delete)](#delete_cookieselfcookie_to_delete)
- [dismiss_alert(self)](#dismiss_alertself)
- [dont_see(self, selectors: [str | list])](#dont_seeselfselectors:[str|list])
- [dont_see_in_current_url(self, search_key: str)](#dont_see_in_current_urlselfsearch_key:str)
- [dont_see_in_title(self, search_key: str)](#dont_see_in_titleselfsearch_key:str)
- [execute_async_js_script(self, js_script, arguments=None)](#execute_async_js_scriptselfjs_scriptarguments=None)
- [execute_js_script(self, js_script, arguments=None)](#execute_js_scriptselfjs_scriptarguments=None)
- [fill_field(self, selector, value)](#fill_fieldselfselectorvalue)
- [fill_form(self, selector_data)](#fill_formselfselector_data)
- [find(self, selector: str)](#findselfselector:str)
- [find_by_class(self, selector: str)](#find_by_classselfselector:str)
- [find_multiply_by_css(self, selector: str)](#find_multiply_by_cssselfselector:str)
- [find_multiply_by_xpath(self, selector: str)](#find_multiply_by_xpathselfselector:str)
- [get_all_cookies(self)](#get_all_cookiesself)
- [get_base_url()](#get_base_url)
- [get_cookie(self, cookie)](#get_cookieselfcookie)
- [get_page_title(self)](#get_page_titleself)
- [get_text_from_element(self, selector)](#get_text_from_elementselfselector)
- [get_timeout()](#get_timeout)
- [maximize_window(self)](#maximize_windowself)
- [move_mouse_on_element(self, selector)](#move_mouse_on_elementselfselector)
- [page_back(self)](#page_backself)
- [page_forward(self)](#page_forwardself)
- [page_refresh(self)](#page_refreshself)
- [press_key(self, key)](#press_keyselfkey)
- [quit(self)](#quitself)
- [resize_window(self, width, height)](#resize_windowselfwidthheight)
- [scroll_to(self, selector)](#scroll_toselfselector)
- [see(self, selectors: [str | list])](#seeselfselectors:[str|list])
- [see_at_least_one(self, selector)](#see_at_least_oneselfselector)
- [see_elements_in_quantity_of(self, selector: str, qty: int)](#see_elements_in_quantity_ofselfselector:strqty:int)
- [see_in_title(self, search_key)](#see_in_titleselfsearch_key)
- [see_in_url(self, search_key: str)](#see_in_urlselfsearch_key:str)
- [see_text(self, text)](#see_textselftext)
- [send_keys(self, selector, keys)](#send_keysselfselectorkeys)
- [set_cookie(self, cookie_name: dict)](#set_cookieselfcookie_name:dict)
- [strict_wait(self, seconds: int)](#strict_waitselfseconds:int)
- [submit_form(self, selector)](#submit_formselfselector)
- [switch_to_default(self)](#switch_to_defaultself)
- [switch_to_frame(self, frame_id)](#switch_to_frameselfframe_id)
- [type_in_alert(self, value)](#type_in_alertselfvalue)
- [wait_for_alert_(self, selector: str)](#wait_for_alert_selfselector:str)
- [wait_for_element_to_be_present_in_dom(self, selector: str)](#wait_for_element_to_be_present_in_domselfselector:str)
- [wait_for_element_to_be_visible(self, selector: str)](#wait_for_element_to_be_visibleselfselector:str)
- [wait_for_element_to_disappear(self, selector: str)](#wait_for_element_to_disappearselfselector:str)
- [wait_for_text_to_be_present_in_element(self, selector: str, text: str)](#wait_for_text_to_be_present_in_elementselfselector:strtext:str)
- [wait_for_text_to_be_present_in_element_attribute(self, selector: str, text_in_attribute: str)](#wait_for_text_to_be_present_in_element_attributeselfselector:strtext_in_attribute:str)
- [wait_for_text_to_be_present_in_element_value(self, selector: str, value_text: str)](#wait_for_text_to_be_present_in_element_valueselfselector:strvalue_text:str)

## accept_alert(self)


        Accepts the alert.

        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 234)
def accept_alert(self) -> return_type:
    """
        Accepts the alert.

        :return: self
        """
    # Function code goes here
```

## by_xpath_or_css(self, selector: str)


        Return tuple with search pattern (XPATH or CSS) and searched selector.

        :param selector: XPATH or CSS selector string
        :return: tuple with search pattern (XPATH or CSS) and searched selector
        

```python
# src/vigilant/actions/finder.py (line 16)
def by_xpath_or_css(self, selector: str) -> return_type:
    """
        Return tuple with search pattern (XPATH or CSS) and searched selector.

        :param selector: XPATH or CSS selector string
        :return: tuple with search pattern (XPATH or CSS) and searched selector
        """
    # Function code goes here
```

## clear_field(self, selector)


        Clears a field after it becomes visible.

        :param selector: The field to clear
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 376)
def clear_field(self, selector) -> return_type:
    """
        Clears a field after it becomes visible.

        :param selector: The field to clear
        :return: self
        """
    # Function code goes here
```

## click(self, selector)


        Clicks on an element after it becomes visible.

        :param selector: The element to click on
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 268)
def click(self, selector) -> return_type:
    """
        Clicks on an element after it becomes visible.

        :param selector: The element to click on
        :return: self
        """
    # Function code goes here
```

## click_with_delay(self, selector, delay=2)


        Clicks on an element only after it becomes visible and adds an additional delay before click.

        :param selector: The element to click on
        :param delay: The additional delay in seconds (default is 2)
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 255)
def click_with_delay(self, selector, delay=2) -> return_type:
    """
        Clicks on an element only after it becomes visible and adds an additional delay before click.

        :param selector: The element to click on
        :param delay: The additional delay in seconds (default is 2)
        :return: self
        """
    # Function code goes here
```

## close(self)


        Closes the current window.

        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 47)
def close(self) -> return_type:
    """
        Closes the current window.

        :return: self
        """
    # Function code goes here
```

## count_elements(self, selector: str)


        Count all elements that match the provided selector, visible or not.

        :param selector: CSS selector
        :return: number of elements that match the selector
        

```python
# src/vigilant/actions/assertions.py (line 29)
def count_elements(self, selector: str) -> return_type:
    """
        Count all elements that match the provided selector, visible or not.

        :param selector: CSS selector
        :return: number of elements that match the selector
        """
    # Function code goes here
```

## delete_all_cookies(self)


        Deletes all cookies in the scope of the session.

        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 152)
def delete_all_cookies(self) -> return_type:
    """
        Deletes all cookies in the scope of the session.

        :return: self
        """
    # Function code goes here
```

## delete_cookie(self, cookie_to_delete)


        Deletes a specific cookie.

        :param cookie_to_delete: The name of the cookie to delete
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 162)
def delete_cookie(self, cookie_to_delete) -> return_type:
    """
        Deletes a specific cookie.

        :param cookie_to_delete: The name of the cookie to delete
        :return: self
        """
    # Function code goes here
```

## dismiss_alert(self)


        Dismisses the alert.

        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 224)
def dismiss_alert(self) -> return_type:
    """
        Dismisses the alert.

        :return: self
        """
    # Function code goes here
```

## dont_see(self, selectors: [str | list])


        Assert that none of the elements matching the provided selectors are visible.

        :param selectors: list of CSS selectors
        

```python
# src/vigilant/actions/assertions.py (line 41)
def dont_see(self, selectors: [str | list]) -> return_type:
    """
        Assert that none of the elements matching the provided selectors are visible.

        :param selectors: list of CSS selectors
        """
    # Function code goes here
```

## dont_see_in_current_url(self, search_key: str)


        Assert that the provided search key is not present in the current page URL.

        :param search_key: string to search for
        

```python
# src/vigilant/actions/assertions.py (line 67)
def dont_see_in_current_url(self, search_key: str) -> return_type:
    """
        Assert that the provided search key is not present in the current page URL.

        :param search_key: string to search for
        """
    # Function code goes here
```

## dont_see_in_title(self, search_key: str)


        Assert that the provided search key is not present in the current page title.

        :param search_key: string to search for
        

```python
# src/vigilant/actions/assertions.py (line 57)
def dont_see_in_title(self, search_key: str) -> return_type:
    """
        Assert that the provided search key is not present in the current page title.

        :param search_key: string to search for
        """
    # Function code goes here
```

## execute_async_js_script(self, js_script, arguments=None)


        Executes an asynchronous JavaScript script with optional arguments.

        :param js_script: The JavaScript script to execute
        :param arguments: Optional arguments for the script
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 140)
def execute_async_js_script(self, js_script, arguments=None) -> return_type:
    """
        Executes an asynchronous JavaScript script with optional arguments.

        :param js_script: The JavaScript script to execute
        :param arguments: Optional arguments for the script
        :return: self
        """
    # Function code goes here
```

## execute_js_script(self, js_script, arguments=None)


        Executes a JavaScript script with optional arguments.

        :param js_script: The JavaScript script to execute
        :param arguments: Optional arguments for the script
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 128)
def execute_js_script(self, js_script, arguments=None) -> return_type:
    """
        Executes a JavaScript script with optional arguments.

        :param js_script: The JavaScript script to execute
        :param arguments: Optional arguments for the script
        :return: self
        """
    # Function code goes here
```

## fill_field(self, selector, value)


        Fills a field with a specified value after the field becomes visible.

        :param selector: The field to fill
        :param value: The value to fill in the field
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 301)
def fill_field(self, selector, value) -> return_type:
    """
        Fills a field with a specified value after the field becomes visible.

        :param selector: The field to fill
        :param value: The value to fill in the field
        :return: self
        """
    # Function code goes here
```

## fill_form(self, selector_data)


        Fills multiple fields in a form using a dictionary of selectors and values.

        :param selector_data: A dictionary of selectors and values
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 314)
def fill_form(self, selector_data) -> return_type:
    """
        Fills multiple fields in a form using a dictionary of selectors and values.

        :param selector_data: A dictionary of selectors and values
        :return: self
        """
    # Function code goes here
```

## find(self, selector: str)


        return self.driver.find_element(*self.by_xpath_or_css(selector))

    def find_multiply(self, selector: str) -> List[WebElement]:
        

```python
# src/vigilant/actions/finder.py (line 46)
def find(self, selector: str) -> return_type:
    """
        return self.driver.find_element(*self.by_xpath_or_css(selector))

    def find_multiply(self, selector: str) -> List[WebElement]:
        """
    # Function code goes here
```

## find_by_class(self, selector: str)


        Find element by class name.

        :param selector: class name string
        :return: the element found using the class name selector
        

```python
# src/vigilant/actions/finder.py (line 68)
def find_by_class(self, selector: str) -> return_type:
    """
        Find element by class name.

        :param selector: class name string
        :return: the element found using the class name selector
        """
    # Function code goes here
```

## find_multiply_by_css(self, selector: str)


        Find multiple elements by CSS selector.

        :param selector: CSS selector string
        :return: list of elements found using the CSS selector
        

```python
# src/vigilant/actions/finder.py (line 37)
def find_multiply_by_css(self, selector: str) -> return_type:
    """
        Find multiple elements by CSS selector.

        :param selector: CSS selector string
        :return: list of elements found using the CSS selector
        """
    # Function code goes here
```

## find_multiply_by_xpath(self, selector: str)


        Find multiple elements by XPATH selector.

        :param selector: XPATH selector string
        :return: list of elements found using the XPATH selector
        

```python
# src/vigilant/actions/finder.py (line 28)
def find_multiply_by_xpath(self, selector: str) -> return_type:
    """
        Find multiple elements by XPATH selector.

        :param selector: XPATH selector string
        :return: list of elements found using the XPATH selector
        """
    # Function code goes here
```

## get_all_cookies(self)


        Returns a set of dictionaries corresponding to cookies visible in the current session.

        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 182)
def get_all_cookies(self) -> return_type:
    """
        Returns a set of dictionaries corresponding to cookies visible in the current session.

        :return: self
        """
    # Function code goes here
```

## get_base_url()


    Get the base URL from the environment variable 'BASE_URL'.

    :return: base URL as a string
    

```python
# src/vigilant/actions/vigilant_actions.py (line 12)
def get_base_url() -> return_type:
    """
    Get the base URL from the environment variable 'BASE_URL'.

    :return: base URL as a string
    """
    # Function code goes here
```

## get_cookie(self, cookie)


        Gets a single cookie.

        :param cookie: The name of the cookie to retrieve
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 192)
def get_cookie(self, cookie) -> return_type:
    """
        Gets a single cookie.

        :param cookie: The name of the cookie to retrieve
        :return: self
        """
    # Function code goes here
```

## get_page_title(self)


        Returns the title of the current page.

        :return: page title as a string
        

```python
# src/vigilant/actions/vigilant_actions.py (line 97)
def get_page_title(self) -> return_type:
    """
        Returns the title of the current page.

        :return: page title as a string
        """
    # Function code goes here
```

## get_text_from_element(self, selector)


        Gets the text from an element after it becomes visible.

        :param selector: The element to get text from
        :return: The text of the element
        

```python
# src/vigilant/actions/vigilant_actions.py (line 290)
def get_text_from_element(self, selector) -> return_type:
    """
        Gets the text from an element after it becomes visible.

        :param selector: The element to get text from
        :return: The text of the element
        """
    # Function code goes here
```

## get_timeout()


        Waits for the element with the specified selector to be clickable.

        :param selector: The element's selector
        :return: self
        

```python
# src/vigilant/actions/waiter.py (line 12)
def get_timeout() -> return_type:
    """
        Waits for the element with the specified selector to be clickable.

        :param selector: The element's selector
        :return: self
        """
    # Function code goes here
```

## maximize_window(self)


        Maximizes the current window that the WebDriver is using.

        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 106)
def maximize_window(self) -> return_type:
    """
        Maximizes the current window that the WebDriver is using.

        :return: self
        """
    # Function code goes here
```

## move_mouse_on_element(self, selector)


        Moves the mouse cursor over an element after the element becomes visible.

        :param selector: The element to move the mouse cursor over
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 328)
def move_mouse_on_element(self, selector) -> return_type:
    """
        Moves the mouse cursor over an element after the element becomes visible.

        :param selector: The element to move the mouse cursor over
        :return: self
        """
    # Function code goes here
```

## page_back(self)


        Goes one step backward in the browser history.

        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 67)
def page_back(self) -> return_type:
    """
        Goes one step backward in the browser history.

        :return: self
        """
    # Function code goes here
```

## page_forward(self)


        Goes one step forward in the browser history.

        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 77)
def page_forward(self) -> return_type:
    """
        Goes one step forward in the browser history.

        :return: self
        """
    # Function code goes here
```

## page_refresh(self)


        Refreshes the current page.

        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 87)
def page_refresh(self) -> return_type:
    """
        Refreshes the current page.

        :return: self
        """
    # Function code goes here
```

## press_key(self, key)


        Presses a specified key.

        :param key: The key to press
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 341)
def press_key(self, key) -> return_type:
    """
        Presses a specified key.

        :param key: The key to press
        :return: self
        """
    # Function code goes here
```

## quit(self)


        Quits the driver and closes every associated window.

        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 57)
def quit(self) -> return_type:
    """
        Quits the driver and closes every associated window.

        :return: self
        """
    # Function code goes here
```

## resize_window(self, width, height)


        Sets the current window width and height.

        :param width: The desired window width in pixels
        :param height: The desired window height in pixels
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 116)
def resize_window(self, width, height) -> return_type:
    """
        Sets the current window width and height.

        :param width: The desired window width in pixels
        :param height: The desired window height in pixels
        :return: self
        """
    # Function code goes here
```

## scroll_to(self, selector)


        Scrolls to an element.

        :param selector: The element to scroll to
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 279)
def scroll_to(self, selector) -> return_type:
    """
        Scrolls to an element.

        :param selector: The element to scroll to
        :return: self
        """
    # Function code goes here
```

## see(self, selectors: [str | list])


        Assert that at least one of the elements matching the provided selectors is visible.

        :param selectors: list of CSS selectors
        

```python
# src/vigilant/actions/assertions.py (line 77)
def see(self, selectors: [str | list]) -> return_type:
    """
        Assert that at least one of the elements matching the provided selectors is visible.

        :param selectors: list of CSS selectors
        """
    # Function code goes here
```

## see_at_least_one(self, selector)


        Assert that at least one element matching the provided selector is visible.

        :param selector: CSS selector
        

```python
# src/vigilant/actions/assertions.py (line 104)
def see_at_least_one(self, selector) -> return_type:
    """
        Assert that at least one element matching the provided selector is visible.

        :param selector: CSS selector
        """
    # Function code goes here
```

## see_elements_in_quantity_of(self, selector: str, qty: int)


        Assert that the number of visible elements that match the provided selector is equal to the provided quantity.

        :param selector: CSS selector
        :param qty: expected number of elements
        

```python
# src/vigilant/actions/assertions.py (line 93)
def see_elements_in_quantity_of(self, selector: str, qty: int) -> return_type:
    """
        Assert that the number of visible elements that match the provided selector is equal to the provided quantity.

        :param selector: CSS selector
        :param qty: expected number of elements
        """
    # Function code goes here
```

## see_in_title(self, search_key)


        Assert that the provided search key is present in the current page title.

        :param search_key: string to search for
        

```python
# src/vigilant/actions/assertions.py (line 114)
def see_in_title(self, search_key) -> return_type:
    """
        Assert that the provided search key is present in the current page title.

        :param search_key: string to search for
        """
    # Function code goes here
```

## see_in_url(self, search_key: str)


        Assert that the provided search key is present in the current page URL.

        :param search_key: string to search for
        

```python
# src/vigilant/actions/assertions.py (line 124)
def see_in_url(self, search_key: str) -> return_type:
    """
        Assert that the provided search key is present in the current page URL.

        :param search_key: string to search for
        """
    # Function code goes here
```

## see_text(self, text)


        Assert that the provided text is present on the current page.

        :param text: text to search for
        

```python
# src/vigilant/actions/assertions.py (line 134)
def see_text(self, text) -> return_type:
    """
        Assert that the provided text is present on the current page.

        :param text: text to search for
        """
    # Function code goes here
```

## send_keys(self, selector, keys)


        Sends keys to a specified field.

        :param selector: The field to send keys to
        :param keys: The keys to send
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 353)
def send_keys(self, selector, keys) -> return_type:
    """
        Sends keys to a specified field.

        :param selector: The field to send keys to
        :param keys: The keys to send
        :return: self
        """
    # Function code goes here
```

## set_cookie(self, cookie_name: dict)


        Sets a new cookie.

        :param cookie_name: A dictionary containing the cookie name and value
        

```python
# src/vigilant/actions/vigilant_actions.py (line 173)
def set_cookie(self, cookie_name: dict) -> return_type:
    """
        Sets a new cookie.

        :param cookie_name: A dictionary containing the cookie name and value
        """
    # Function code goes here
```

## strict_wait(self, seconds: int)


        Waits for the specified number of seconds.

        :param seconds: The number of seconds to wait
        :return: self
        

```python
# src/vigilant/actions/waiter.py (line 129)
def strict_wait(self, seconds: int) -> return_type:
    """
        Waits for the specified number of seconds.

        :param seconds: The number of seconds to wait
        :return: self
        """
    # Function code goes here
```

## submit_form(self, selector)


        Submits a form using a specified selector.

        :param selector: The form to submit
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 365)
def submit_form(self, selector) -> return_type:
    """
        Submits a form using a specified selector.

        :param selector: The form to submit
        :return: self
        """
    # Function code goes here
```

## switch_to_default(self)


        Switches the WebDriver focus to the default frame.

        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 214)
def switch_to_default(self) -> return_type:
    """
        Switches the WebDriver focus to the default frame.

        :return: self
        """
    # Function code goes here
```

## switch_to_frame(self, frame_id)


        Switches the WebDriver focus to the specified frame.

        :param frame_id: The ID of the frame to switch to
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 203)
def switch_to_frame(self, frame_id) -> return_type:
    """
        Switches the WebDriver focus to the specified frame.

        :param frame_id: The ID of the frame to switch to
        :return: self
        """
    # Function code goes here
```

## type_in_alert(self, value)


        Types the specified value in the alert.

        :param value: The value to type in the alert
        :return: self
        

```python
# src/vigilant/actions/vigilant_actions.py (line 244)
def type_in_alert(self, value) -> return_type:
    """
        Types the specified value in the alert.

        :param value: The value to type in the alert
        :return: self
        """
    # Function code goes here
```

## wait_for_alert_(self, selector: str)


        Waits for an alert to be present.

        :param selector: The element's selector
        :return: self
        

```python
# src/vigilant/actions/waiter.py (line 116)
def wait_for_alert_(self, selector: str) -> return_type:
    """
        Waits for an alert to be present.

        :param selector: The element's selector
        :return: self
        """
    # Function code goes here
```

## wait_for_element_to_be_present_in_dom(self, selector: str)


        Waits for the element with the specified selector to be present in the DOM.

        :param selector: The element's selector
        :return: self
        

```python
# src/vigilant/actions/waiter.py (line 48)
def wait_for_element_to_be_present_in_dom(self, selector: str) -> return_type:
    """
        Waits for the element with the specified selector to be present in the DOM.

        :param selector: The element's selector
        :return: self
        """
    # Function code goes here
```

## wait_for_element_to_be_visible(self, selector: str)


        Waits for the element with the specified selector to be visible.

        :param selector: The element's selector
        :return: self
        

```python
# src/vigilant/actions/waiter.py (line 35)
def wait_for_element_to_be_visible(self, selector: str) -> return_type:
    """
        Waits for the element with the specified selector to be visible.

        :param selector: The element's selector
        :return: self
        """
    # Function code goes here
```

## wait_for_element_to_disappear(self, selector: str)


        Waits for the element with the specified selector to disappear.

        :param selector: The element's selector
        :return: self
        

```python
# src/vigilant/actions/waiter.py (line 61)
def wait_for_element_to_disappear(self, selector: str) -> return_type:
    """
        Waits for the element with the specified selector to disappear.

        :param selector: The element's selector
        :return: self
        """
    # Function code goes here
```

## wait_for_text_to_be_present_in_element(self, selector: str, text: str)


        Waits for the specified text to be present in the element with the given selector.

        :param selector: The element's selector
        :param text: The text to wait for
        :return: self
        

```python
# src/vigilant/actions/waiter.py (line 88)
def wait_for_text_to_be_present_in_element(self, selector: str, text: str) -> return_type:
    """
        Waits for the specified text to be present in the element with the given selector.

        :param selector: The element's selector
        :param text: The text to wait for
        :return: self
        """
    # Function code goes here
```

## wait_for_text_to_be_present_in_element_attribute(self, selector: str, text_in_attribute: str)


        Waits for the specified text to be present in the attribute of the element with the given selector.

        :param selector: The element's selector
        :param text_in_attribute: The text to wait for
        :return: self
        

```python
# src/vigilant/actions/waiter.py (line 102)
def wait_for_text_to_be_present_in_element_attribute(self, selector: str, text_in_attribute: str) -> return_type:
    """
        Waits for the specified text to be present in the attribute of the element with the given selector.

        :param selector: The element's selector
        :param text_in_attribute: The text to wait for
        :return: self
        """
    # Function code goes here
```

## wait_for_text_to_be_present_in_element_value(self, selector: str, value_text: str)


        Waits for the specified text to be present in the value of the element with the given selector.

        :param selector: The element's selector
        :param value_text: The text to wait for
        :return: self
        

```python
# src/vigilant/actions/waiter.py (line 74)
def wait_for_text_to_be_present_in_element_value(self, selector: str, value_text: str) -> return_type:
    """
        Waits for the specified text to be present in the value of the element with the given selector.

        :param selector: The element's selector
        :param value_text: The text to wait for
        :return: self
        """
    # Function code goes here
```

