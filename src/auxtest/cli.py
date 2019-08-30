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
)
def cli(loglevel):
    """Script entrypoint, write command line help text here.

    For more info on how a click arg parser is written and documented, check
    out the official docs: https://click.palletsprojects.com/en/7.x/
    """
    setup_logging(loglevel)
    log.info(f"Running auxtest.cli with loglevel {loglevel}.")


@cli.command()
@cli.argument("--host", type=str)
@cli.argument("--debug", type=bool)
def run(host, debug):
    api.app.run(host=host, debug=debug)
