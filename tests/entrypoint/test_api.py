"""Can't unit test routes, so do some functional testing instead."""
import json
from pathlib import Path

import pytest

from auxtest.settings import VERSION
from ..conftest import TEST_DIR

fixtures = []
for path in Path(TEST_DIR / 'fixtures' / 'main_api').iterdir():
    with path.open() as fixture_file:
        fx = json.load(fixture_file)
    fixtures.append(pytest.param(fx['query'], fx['response'], id=path.name))


def test_route_to_status(entrypoint):
    response = entrypoint.get('/').json
    assert response['msg'] == f"Service is running, version: {VERSION}."


@pytest.mark.parametrize('query, response', fixtures)
def test_route_to_check(entrypoint, query, response):
    test_response = entrypoint.get(query).json
    if test_response == response:
        assert test_response == response
    else:
        for key in response:
            if isinstance(response[key], dict):
                assert response[key].items() <= test_response[key].items()
            else:
                assert response[key] == test_response[key]
