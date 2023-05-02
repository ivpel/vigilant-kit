import click
from .install_webdriver_command import check_version_and_download_driver
from .install_standalone_command import check_req_and_install_selenium_server


@click.command(name='dev-kit', help="Install local development kit (Webdriver, Selenium Server, etc)")
@click.option('-b', '--browser', type=click.Choice(['chrome', 'firefox', 'edge']), required=True)
def install_dev_kit(browser):
    check_version_and_download_driver(browser)
    check_req_and_install_selenium_server()


if __name__ == "__main__":
    install_dev_kit()
