# Running browsers (local vs remote)

Vigilant Kit can run against a **local** browser or a **remote** Selenium server / Grid.

## Option 1 (recommended): Local browser (no Selenium server)

Set:
```shell
export SELENIUM_HOST=local
export SELENIUM_BROWSER=chrome   # or firefox
```

Selenium 4 can automatically manage browser drivers (Selenium Manager). If your machine has Chrome/Firefox installed,
this is usually all you need.

## Option 2: Remote Selenium / Grid (Docker)

If you prefer a remote server, Docker Selenium is the easiest local setup:

```shell
docker run -d --rm -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome
```

Or Firefox:

```shell
docker run -d --rm -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox
```

Then configure Vigilant:

```shell
export SELENIUM_HOST=http://127.0.0.1:4444/wd/hub
export SELENIUM_BROWSER=chrome   # or firefox
```

The official images and options are documented here: [Docker Selenium](https://github.com/SeleniumHQ/docker-selenium).
