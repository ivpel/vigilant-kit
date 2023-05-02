#!/usr/bin/env python

import click
from .install_webdriver_command import install_webdriver
from .install_standalone_command import install_selenium_standalone
from .install_dev_kit_command import install_dev_kit


@click.group(name="vgl.py")
def vgl():
    pass


vgl.add_command(install_webdriver)
vgl.add_command(install_selenium_standalone)
vgl.add_command(install_dev_kit)
vgl()
