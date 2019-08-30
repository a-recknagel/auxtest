"""Auxtest Web Service API.

All routes (and nothing else) are defined here.

Notes:
    * Doesn't support authentication yet, so not safe for usage outside of
      intranets.
    * The current cli.py starts the dev server, which isn't stable
      enough for production purposes.
    * Discuss if acceptance criteria of retuning json instead of error code
      is ok.

"""
from logging import getLogger

from flask import Flask, jsonify, request, Response

from auxtest.checks.check_funcs import daytemp, naming, rival
from auxtest import __version__

log = getLogger(__name__)
app = Flask(__name__)
CITY_KWARG = "city"


@app.route("/", methods=["GET"])
def route_to_status() -> str:
    """Show status of service.

    Returns:
        A status message and the current version.

    """
    log.debug("Status checked.")
    return jsonify({"msg": f"Service is running, version: {__version__}."})


@app.route("/check", methods=["GET"])
def route_to_city_check() -> Response:
    """Invoke check function.

    Given a city name, run a number of check functions and return their
    individual and cumulative results. The cumulative logical connector is an
    and operation of all checks. An example result could be:

    >>> {
    ...     'check': False,
    ...     'criteria': {'naming': True, 'daytemp': False, 'rival': True}
    ... }

    And in case of an error:

    >>> {'error': True}

    Returns:
        Response: Flask.Response with the result rendered as a json.

    """
    log.debug("Received check-request.")

    # checking if city name was set
    if CITY_KWARG not in request.args or not request.args[CITY_KWARG]:
        log.info(f"Aborting, no city specified in kwargs: " f"'{ {**request.args} }'")
        return jsonify({"error": True})
    else:
        city = request.args[CITY_KWARG]

    log.debug("Calling check functions...")
    try:
        check_naming = naming(city)
        check_daytemp = daytemp(city)
        check_rival = rival(city)
    except ValueError as e:
        log.warning(f"Aborting, something went wrong in the check-funcs: '{e}'")
        return jsonify({"error": True})
    return jsonify(
        {
            "check": check_naming and check_daytemp and check_rival,
            "criteria": {
                "naming": check_naming,
                "daytemp": check_daytemp,
                "check_rival": check_rival,
            },
        }
    )
