import subprocess
import click
import psutil

SELENIUM_SERVER_JAR = "selenium-server/selenium-server-standalone.jar"


def find_selenium_server_process():
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        if process.info['name'] == 'java' and SELENIUM_SERVER_JAR in process.info['cmdline']:
            return process
    return None


@click.command(name='run', help="Run Selenium Server JAR file")
@click.option('--port', '-p', type=int, default=4444, help="Port number for the server")
@click.option('--driver', '-D', multiple=True,
              help="Specify driver options (e.g. -Dwebdriver.chrome.driver=chromedriver)")
@click.option('--daemon', '-d', is_flag=True, help="Run the server as a daemon")
def run_selenium_server(port, driver, daemon):
    driver_options = " ".join(driver)
    cmd = ["java", "-jar", SELENIUM_SERVER_JAR, "-port", str(port)]
    cmd.extend(driver_options.split())

    click.echo(f"Running Selenium Server with command:\n {' '.join(cmd)}")

    if daemon:
        # Start the process in the background (daemon mode) using subprocess.Popen
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        click.echo(f"Selenium Server is running in daemon mode with PID: {process.pid}")
    else:
        # Start the process in the foreground and wait for it to finish using subprocess.run
        subprocess.run(cmd)


@click.command(name='stop', help="Stop the running Selenium Server")
def stop_selenium_server():
    selenium_server_process = find_selenium_server_process()
    if selenium_server_process:
        pid = selenium_server_process.info['pid']
        try:
            selenium_server_process.terminate()
            click.echo(f"Selenium Server with PID {pid} has been stopped.")
        except psutil.NoSuchProcess:
            click.echo(f"Failed to stop Selenium Server. Process with PID {pid} does not exist.")
    else:
        click.echo("Selenium Server is not running in daemon mode.")
