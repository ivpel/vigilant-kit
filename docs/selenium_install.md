# How to install Selenium Server & browser drivers

***
## Option 1: Run Selenium server + browser driver locally
###  1. Install Selenium Standalone Server and Webdriver
`vgl install dev-kit -b chrome`

If everything is okay and your machine has all dependencies installed, you will see this output:
```text
Found: chrome browser, version 112.0.5615.165.
Downloading driver for chrome browser ... OK
Downloading Selenium Standalone server ...OK
```

### 2. Run Selenium Server
To run your Selenium Server use:
`vgl run selenium-server`

This command will launch Selenium Standalone server on your local machine.

### Need help? Use `--help`
To see all available options for these commands you can use `--help` flag.

For example:
`vgl run selenium-server --help`

Will output this:
```text
Usage: vgl run selenium-server [OPTIONS]

  Run Selenium Server JAR file

Options:
  -p, --port INTEGER  Port number for the server
  -D, --driver TEXT   Specify driver options (e.g.
                      -Dwebdriver.chrome.driver=chromedriver)
  -d, --daemon        Run the server as a daemon
  --help              Show this message and exit.
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
