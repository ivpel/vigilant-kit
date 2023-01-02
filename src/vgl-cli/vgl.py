#!/usr/bin/env python

import click
from local_dev import install_selenium_dev_server


@click.group(name="vgl")
def vgl():
    pass


if __name__ == '__main__':
    vgl.add_command(install_selenium_dev_server)
    vgl()
