import os
import sys
import tarfile
import click
from .utils import download_file


def install_selenium():
    try:
        click.echo("Creating directory for Selenium server...", nl=False)
        os.mkdir('selenium')
        os.chdir('selenium')
        click.secho("OK", fg='green')

        # Download Selenium jar file
        click.echo("Downloading Selenium jar file...", nl=False)
        download_file('https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.7.0/selenium-server-4.7.2.jar')
        click.secho("OK", fg='green')

    except FileExistsError:
        click.secho("Error", fg='red')
        click.secho("Directory 'selenium' already exist!", fg='red')
        sys.exit(1)


def install_webdriver(browser):
    chromedriver = "https://chromedriver.storage.googleapis.com/108.0.5359.71/chromedriver_linux64.zip"
    geckodriver = "https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz"
    try:
        click.echo(f"Downloading driver for browser {browser}...", nl=False)
        if browser == "chrome":
            download_file(chromedriver)
        elif browser == "firefox":
            download_file(geckodriver)
            file = tarfile.open('geckodriver-v0.32.0-linux64.tar.gz')
            file.extractall('.')

        click.secho("OK", fg='green')
    except FileNotFoundError as e:
        click.secho("Error", fg='red')
        click.echo(e)


@click.command(name='install:dev-server')
@click.option('--browser', default='firefox', help='Browser which will be used for testing.')
def install_selenium_dev_server(browser):
    install_selenium()
    install_webdriver(browser)
    click.secho("Installation complete.", fg='green')
    click.secho(f"INFO: Before running your Selenium Server locally, make sure that your {browser} browser is updated "
                f"to the last stable version!")
