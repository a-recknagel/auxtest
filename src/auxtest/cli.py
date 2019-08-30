"""Command Line Interface for auxtest.

This module contains no business logic, it only exposes it.
"""
from logging import getLogger

import click

from auxtest.entrypoint import api
from auxtest.util import setup_logging

log = getLogger(__name__)


@click.group()
@click.option(
    "--loglevel",
    default="INFO",
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR"]),
    help="Set the loglevel.",
)
def cli(loglevel):
    """Exposed user API of the auxtest package.

    Currently, auxtest allows you to start a server that wraps some
    simple test-functionality around the weather API. I wrote it to
    try and test some webapp stuff.
    """
    setup_logging(loglevel)
    log.info(f"Running auxtest.cli with loglevel {loglevel}.")


@cli.command()
@click.option("--host", type=str, default="0.0.0.0", help="Target host address.")
@click.option("--debug", is_flag=True, help="Sets debug mode.")
def run(host, debug):
    """Run a flask dev server.

    Flask brings a dev server along, which can be used to test and debug
    the implemented functionality. This command lets you run it, optionally
    providing a custom host address over the default or a flag to enable
    debug mode.
    """
    api.app.run(host=host, debug=debug)
