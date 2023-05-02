import click
import os
import requests

SELENIUM_SERVER_URL = "https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar"
SELENIUM_SERVER_FILE = "selenium-server/selenium-server-standalone.jar"


def check_selenium_requirements():
    java_path = os.popen("which java").read().strip()
    if not java_path:
        click.secho("Java is not installed on this machine.", fg="red")
        return False

    java_version = os.popen("java -version 2>&1 | awk -F '\"' '/version/ {print $2}'").read().strip()
    major_version = java_version.split('.')[0]
    if int(major_version) < 9:
        click.secho(f"Java version {java_version} is not supported. Please install Java 9 or higher.", fg="red")
        return False

    return True


def download_selenium_server():
    response = requests.get(SELENIUM_SERVER_URL)
    os.makedirs("selenium-server", exist_ok=True)
    with open(SELENIUM_SERVER_FILE, "wb") as f:
        f.write(response.content)


def check_req_and_install_selenium_server():
    if check_selenium_requirements():
        click.secho("Downloading Selenium Standalone server ...", nl=False)
        download_selenium_server()
        click.secho("OK", fg="green")


@click.command(name="standalone", help="Install Selenium Standalone server.")
def install_selenium_standalone():
    check_req_and_install_selenium_server()


if __name__ == "__main__":
    install_selenium_standalone()
