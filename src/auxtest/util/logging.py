"""Collection of utility functions.

This module should be importable without causing problems, so no objects may be
created when it is loaded - except those on settings.py.
"""
import json
from logging import config
import traceback

from auxtest.settings import CWD


def configure_logger():
    """Set up the logger.

    These print statements here should be the only ones in the entire codebase.
    This code should be run before any parts of the application itself.
    """
    try:
        with open(CWD / 'logger_config.json') as conf_file:
            cfg = json.load(conf_file)
    except (IsADirectoryError, IOError, FileNotFoundError, PermissionError,
            ValueError) as e:
        print("Something went wrong while loading the logger config. Make sure "
              "it exists and is well-formed. Using NullHandler instead.")
        print(traceback.print_tb(e.__traceback__))
        cfg = {
            'version': 1,
            'disable_existing_loggers': True,
            'handlers': {
                'null': {'level': 'DEBUG', 'class': 'logging.NullHandler'}
            }
        }
    config.dictConfig(cfg)
