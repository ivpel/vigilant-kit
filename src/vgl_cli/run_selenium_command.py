import os
import click

SELENIUM_SERVER_JAR = "selenium-server/selenium-server-standalone.jar"


@click.command(name='selenium-server', help="Run Selenium Server JAR file")
@click.option('--port', '-p', type=int, default=4444, help="Port number for the server")
@click.option('--driver', '-D', multiple=True,
              help="Specify driver options (e.g. -Dwebdriver.chrome.driver=chromedriver)")
@click.option('--daemon', '-d', is_flag=True, help="Run the server as a daemon")
def run_selenium_server(port, driver, daemon):
    driver_options = " ".join(driver)
    cmd = f"java -jar {SELENIUM_SERVER_JAR} -port {port} {driver_options}"
    click.echo(f"Running Selenium Server with command:\n {cmd}")
    if daemon:
        cmd += " &"
    os.system(cmd)


if __name__ == "__main__":
    run_selenium_server()
