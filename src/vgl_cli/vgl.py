#!/usr/bin/env python

import click
from .install_webdriver_command import install_webdriver
from .install_standalone_command import install_selenium_standalone
from .install_dev_kit_command import install_dev_kit

from .selenium_commands import run_selenium_server, stop_selenium_server


@click.group(name="vgl.py")
def vgl():
    pass


@click.group(name="install", help="Install commands")
def install_group():
    pass


@click.group(name="selenium", help="Run commands")
def selenium_group():
    pass


selenium_group.add_command(run_selenium_server)
selenium_group.add_command(stop_selenium_server)


install_group.add_command(install_webdriver)
install_group.add_command(install_selenium_standalone)
install_group.add_command(install_dev_kit)

vgl.add_command(install_group)
vgl.add_command(selenium_group)


if __name__ == '__main__':
    vgl()
