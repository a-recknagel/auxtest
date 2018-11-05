"""Collection of check functions that can be called in the check-route.

Right now their names are equal to the names of their return keys, so we might
chose to streamline some of the logic to make this very configurable. It would
nail this app to only support keyword arguments that conform to python's
function naming rules, so it might be a bad call to nail this down just yet.

Notes:
    * Might extend the call api with the 'country' kwarg to disambiguate in
      case there are many cities with the submitted name.

"""

from datetime import datetime, time
from urllib.parse import unquote

import requests
from requests import get

from auxtest.settings import (
    DAY_TEMP, NIGHT_TEMP, RIVAL_CITY, SUNDOWN, SUNRISE, WEATHER_API_KEY,
    WEATHER_API_UNITS, WEATHER_API_URL)


def naming(city: str) -> bool:
    """Check whether the input string has an uneven number of characters.

    Only those characters count that are part of the city's name. Python 3 makes
    this part easy (in particular when hosted on linux, where the default for
    locales is UTF-8), because strings are always handled as proper unicode
    character sequences and not byte arrays. So stuff like len('ü') returning
    2 doesn't happen.
    In case ascii descriptions of utf-8 encodings are used, this function
    unquotes them before computing their length, since that is assumed to be the
    more sane behavior.

    Args:
        city: The name of a city.

    Returns:
        True iff the number of characters is uneven.

    """
    city_name = unquote(city).split(',')[0]  # comas are not allowed in queries
    return (len(city_name.strip()) % 2) == 1


def run_weathermap_query(city: str, appid: str, url: str) -> dict:
    """Help function to handle get-requests to the weathermap API.

    Args:
        city: The name of a city.
        appid: API token used to authenticate this service against it.
        url: Base API url where we acquire temperature measurement.

    Returns:
        The json output from the request.

    Raises:
        ValueError in case something goes wrong with the weather request.

    """
    payload = {
        'q': city,
        'appid': appid,
        'units': WEATHER_API_UNITS,
    }
    try:
        res = get(url, payload)
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Can't acquire request: {type(e).__name__} - {e}")
    if res.status_code != 200:
        raise ValueError(f"Invalid status: {res.text}")
    return res.json()


def daytemp(city: str,
            appid: str = WEATHER_API_KEY,
            url: str = WEATHER_API_URL) -> bool:
    """Check if the current temperature conforms to a daytime/nightime setting.

    The expected ranges can be looked up in the settings file, and this function
    only returns True if the temperature is strictly in-between the ranges. For
    example, given the daytime setting (17, 25) and a measurement of 17 at the
    target's daytime, the expected result is False.

    Args:
        city: The name of a city.
        appid: API token used to authenticate this service against it.
        url: Base API url where we acquire temperature measurement.

    Returns:
        True iff the temperature is in-between the expected range.

    Raises:
        ValueError in case something goes wrong with the weather request.

    """
    temperature = run_weathermap_query(city, appid, url)

    # day or night?
    dt_of_measure = datetime.utcfromtimestamp(temperature['dt'])
    dt_comp = time(dt_of_measure.hour, dt_of_measure.minute)
    day_time = SUNRISE < dt_comp < SUNDOWN

    if day_time:
        return DAY_TEMP[0] < temperature['main']['temp'] < DAY_TEMP[1]
    else:
        return NIGHT_TEMP[0] < temperature['main']['temp'] < NIGHT_TEMP[1]


def rival(city: str,
          rival_city: str = RIVAL_CITY,
          appid: str = WEATHER_API_KEY,
          url: str = WEATHER_API_URL) -> bool:
    """Check if the current temperature is higher than the rival's.

    The rival can be defaulted in the settings file, or set explicitly in this
    function.

    Args:
        city: The name of a city.
        rival_city: The name of a rival city.
        appid: API token used to authenticate this service against it.
        url: Base API url where we acquire temperature measurement.

    Returns:
        True iff the city is currently warmer than the rival.

    Raises:
        ValueError in case something goes wrong with the weather request.

    """
    temperature = run_weathermap_query(city, appid, url)
    rival_temperature = run_weathermap_query(rival_city, appid, url)

    return temperature['main']['temp'] > rival_temperature['main']['temp']
