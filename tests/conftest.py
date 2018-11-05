import json
from pathlib import PurePath
import warnings

import pytest

TEST_DIR = PurePath(__file__).parent
RESPONSE_QUEUE = iter([])


@pytest.fixture
def add_responses():
    """Allow to add responses to be consumed by request_get."""
    def inner(*args):
        global RESPONSE_QUEUE
        RESPONSE_QUEUE = iter(args)
    return inner


@pytest.fixture
def request_get():
    """Pretend to be a requests object that supports get().json()."""
    def jsonify():
        response = next(RESPONSE_QUEUE)
        with open(TEST_DIR / 'fixtures' / 'weather_map' / response) as fixture:
            return json.load(fixture)
    ret = type('', (), {})()  # anonymous object
    ret.json = jsonify
    ret.status_code = 200
    return lambda *args, **kwargs: ret


@pytest.fixture
def entrypoint():
    from auxtest.entrypoint.api import app
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore')
        return app.test_client()
