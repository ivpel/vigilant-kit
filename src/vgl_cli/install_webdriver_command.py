import click
import os
import platform
import requests
import tarfile
import zipfile

BROWSER_VERSIONS = {
    "chrome": "https://chromedriver.storage.googleapis.com/LATEST_RELEASE",
    "firefox": "https://api.github.com/repos/mozilla/geckodriver/releases/latest",
    "edge": "https://msedgedriver.azureedge.net/LATEST_RELEASE"
}


def get_browser_version(browser):
    if browser == "chrome":
        # Get the latest version of Chrome from the output of the "google-chrome --version" command
        chrome_version = os.popen("google-chrome --version").read().strip().split()[-1]
        return chrome_version
    elif browser == "firefox":
        # Get the latest version of Firefox from the output of the "firefox --version" command
        firefox_version = os.popen("firefox --version").read().strip().split()[-1]
        return firefox_version.split('.')[0]
    elif browser == "edge":
        try:
            # Get the latest version of Edge from the output of the "msedge --version" command
            edge_version = os.popen("msedge --version").read().strip().split()[-1]
            return edge_version.split('.')[0]
        except IndexError:
            click.echo(f"Failed to get {browser} version")
            return None
    else:
        click.echo(f"{browser} is not a supported browser")
        return None


def download_driver(browser, version):
    download_url = None
    if browser in BROWSER_VERSIONS:
        if browser == "chrome":
            # Get the major version of the Chrome browser installed on the machine
            chrome_version = get_browser_version(browser)
            if chrome_version is None:
                click.secho(f"{browser} is not installed on this machine.", fg="red")
                return
            # Use the ChromeDriver API to get the latest version of the ChromeDriver that is compatible with the installed Chrome browser
            response = requests.get(f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{chrome_version.split('.')[0]}")
            if response.status_code == 200:
                latest_version = response.text
                download_url = f"https://chromedriver.storage.googleapis.com/{latest_version}/chromedriver_{platform.system().lower()}64.zip"
            else:
                click.secho(f"Could not find latest {browser} driver version.", fg="red")
        elif browser == "firefox":
            r = requests.get(BROWSER_VERSIONS[browser])
            release_info = r.json()
            for asset in release_info["assets"]:
                if platform.system().lower() in asset["name"] and "tar.gz" in asset["name"]:
                    download_url = asset["browser_download_url"]
                    break
            else:
                click.secho(f"Could not find latest {browser} driver version... Fail", fg="red")
        elif browser == "edge":
            download_url = f"https://msedgedriver.azureedge.net/{version}/edgedriver_{platform.system().lower()}.zip"
        else:
            click.secho(f"Invalid browser name '{browser}'", fg="red")
            return
    else:
        click.secho(f"Could not find browser '{browser}'.", fg="red")
        return

    if download_url is not None:
        response = requests.get(download_url)
        if download_url.endswith(".zip"):
            with open(f"selenium-server/{browser}_driver.zip", "wb") as f:
                f.write(response.content)
            with zipfile.ZipFile(f"selenium-server/{browser}_driver.zip", 'r') as zip_ref:
                for member in zip_ref.namelist():
                    zip_ref.extract(member, f"selenium-server/{browser}_driver/")
        elif download_url.endswith(".tar.gz"):
            with open(f"selenium-server/{browser}_driver.tar.gz", "wb") as f:
                f.write(response.content)
            with tarfile.open(f"selenium-server/{browser}_driver.tar.gz", 'r:gz') as tar_ref:
                tar_ref.extractall(f"selenium-server/{browser}_driver/")
    else:
        click.secho(f"Could not find download URL for {browser} driver.", fg="red")


def check_version_and_download_driver(browser):
    version = get_browser_version(browser)
    if version is None:
        click.secho(f"{browser} is not installed on this machine", fg="red")
    else:
        click.secho(f"Found: {browser} browser, version {version}.", fg="cyan")
        # Download the driver for the browser
        click.echo(f"Downloading driver for {browser} browser ... ", nl=False)
        download_driver(browser, version)
        click.secho("OK", fg="green")


@click.command(name='webdriver', help="Install the webdriver for a chosen browser.")
@click.option('-b', '--browser', type=click.Choice(['chrome', 'firefox', 'edge']), required=True)
def install_webdriver(browser):
    # Create the selenium-server directory if it doesn't exist
    os.makedirs("selenium-server", exist_ok=True)

    # Check if the browser is installed and get its version
    check_version_and_download_driver(browser)


if __name__ == "__main__":
    install_webdriver()
