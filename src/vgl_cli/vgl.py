#!/usr/bin/env python

import click
from .local_dev import install_selenium_dev_server


@click.group(name="vgl.py")
def vgl():
    pass


vgl.add_command(install_selenium_dev_server)
vgl()
