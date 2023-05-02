#!/usr/bin/env python

import click
from .install_webdriver_command import install_webdriver
from .install_standalone import install_selenium_standalone


@click.group(name="vgl.py")
def vgl():
    pass


vgl.add_command(install_webdriver)
vgl.add_command(install_selenium_standalone)
vgl()
