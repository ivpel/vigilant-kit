# How to install Selenium Server & browser drivers

***
## Option 1: Run Selenium server + browser driver locally
### 1. Install Selenium server
Selenium server is simply a jar file. To install (download) it, just run this command in the root directory
of your project or root directory of your tests
```shell
mkdir selenium-server && cd selenium && wget https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.6.0/selenium-server-4.6.0.jar && cd -
```
### 2. Install browser driver
You will also need to download Selenium driver for the browser where you want to execute the tests. This driver is used
by Selenium server to start the browser of your choice - see following table for the most common browsers:

| Browser | Driver              | Download link                                                                     |
|---------|---------------------|-----------------------------------------------------------------------------------|
| Firefox | Geckodriver         | [Download](https://github.com/mozilla/geckodriver/releases)                       |
| Chrome  | Chromedriver        | [Download](https://sites.google.com/a/chromium.org/chromedriver/downloads)        |
| MS Edge | Microsoft WebDriver | [Download](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) |

Download the browser driver and place the binary file (like geckodriver or chromedriver) to the `selenium-server/` 
directory (where our selenium standalone server is located).
You can also place the file elsewhere, but then you must pass the path to the Selenium server, but as for me, it is easier
to have server and driver binaries in one place.

### 3. Start Selenium server
To start the Selenium server listening for incoming connections simply run:
```shell
java -jar selenium-server/selenium-server-4.6.0.jar
```

## Option 2: Start Selenium server + browser inside Docker
***
If you don't want to install and run Selenium server and the browser locally, you can run both of them in a Docker 
container. The Selenium project provides many prepared official containers.
For example to start a container with Selenium server and Firefox, simply run:
```shell
docker run -d -p 4446:4444 -p 7902:7900 --shm-size="2g" selenium/standalone-firefox:4.6.0-20221104
```

For more info about available options check official [Docker Selenium](https://github.com/SeleniumHQ/docker-selenium) page.
