"""Global utility functions and settings.

Can be used as a configuration file during development, where the
dependencies that turn out to be an issue to update during production or
tests can be adapted to support a more dynamic injection.

Also contains globally relevant utility functions that do not contain
business specific logic.
"""
from logging import getLogger
from logging.config import dictConfig
from datetime import time
from pathlib import Path, PurePath

log = getLogger(__name__)


# useful references
#: Project root
ROOT_DIR = PurePath(__file__).parent.parent
#: Current working directory
CWD = Path.cwd()

# basic weather api settings
#: Request key
WEATHER_API_KEY = "8ca1bf554fe26dff41d635d4e2f866ed"
#: URL base
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
#: Measuring unit type
WEATHER_API_UNITS = "metric"

# day temperature configuration
#: When the sun goes up
SUNRISE = time(6, 0)
#: When it goes down
SUNDOWN = time(18, 0)
#: What we assume to be daytime temperatures
DAY_TEMP = (17, 25)
#: What we assume to be nightime temperatures
NIGHT_TEMP = (10, 15)

#: Default Rival
RIVAL_CITY = "Köln"


def setup_logging(loglevel: str = "INFO"):
    """Set up basic logging to stdout.

    Args:
        loglevel: Can be any of [DEBUG, INFO, WARNING, ERROR, CRITICAL]

    """
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
                }
            },
            "handlers": {
                "default": {
                    "level": loglevel,
                    "formatter": "standard",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                }
            },
            "loggers": {
                "": {"handlers": ["default"], "level": loglevel, "propagate": True}
            },
        }
    )
