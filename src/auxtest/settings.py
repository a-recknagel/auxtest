"""Settings for this project.

Can be used as a stand-in configuration file during development, where the
dependencies that turn out to be an issue to update during production or tests
can be adapted to support a more dynamic injection.
"""
from datetime import time
from pathlib import Path, PurePath


# current software version
VERSION = '1.0.0'

# good to know
ROOT_DIR = PurePath(__file__).parent.parent
CWD = Path.cwd()

# basic weather api settings
WEATHER_API_KEY = '8ca1bf554fe26dff41d635d4e2f866ed'
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather'
WEATHER_API_UNITS = 'metric'

# day-temp configuration
SUNRISE = time(6, 0)
SUNDOWN = time(18, 0)
DAY_TEMP = (17, 25)
NIGHT_TEMP = (10, 15)

# rival
RIVAL_CITY = 'Köln'
