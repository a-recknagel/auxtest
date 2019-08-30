import pytest
import requests

from auxtest.checks.check_funcs import daytemp, naming, rival, run_weathermap_query


def test_naming():
    assert naming("Berlin") is False
    assert naming("Stuttgart") is True
    assert naming("Gießen") is False
    assert naming("München") is True
    assert naming("Düsseldorf") is False
    assert naming("Düsseldorf,de") is False  # sneaky


def test_rival(monkeypatch, request_get, add_responses):
    from auxtest.checks import check_funcs

    monkeypatch.setattr(check_funcs, "get", request_get)

    add_responses("warm_day.json", "cold_day.json")
    assert rival("points to warm_day", "points to cold_day") is True
    add_responses("cold_day.json", "warm_day.json")
    assert rival("points to cold_day", "points to warm_day") is False
    add_responses("chilly_day.json", "chilly_day.json")
    assert rival("points to chilly_day", "points to chilly_day") is False
    add_responses("chilly_day.json", "cold_night.json")
    assert rival("points to chilly_day", "points to cold_night") is True


def test_daytemp(monkeypatch, request_get, add_responses):
    from auxtest.checks import check_funcs

    monkeypatch.setattr(check_funcs, "get", request_get)

    add_responses("cold_day.json")
    assert daytemp("points to cold_day") is False
    add_responses("cold_night.json")
    assert daytemp("points to cold_night") is False
    add_responses("chilly_day.json")
    assert daytemp("points to chilly_day") is False
    add_responses("chilly_night.json")
    assert daytemp("points to chilly_night") is True
    add_responses("warm_day.json")
    assert daytemp("points to warm_day") is True
    add_responses("warm_night.json")
    assert daytemp("points to warm_night") is False
    add_responses("hot_day.json")
    assert daytemp("points to hot_day") is False
    add_responses("hot_night.json")
    assert daytemp("points to hot_night") is False


def test_run_weathermap_query(monkeypatch):
    from auxtest.checks import check_funcs

    def throws(*_, **__):
        raise requests.exceptions.RequestException()

    monkeypatch.setattr(check_funcs, "get", throws)
    with pytest.raises(ValueError):
        run_weathermap_query("raises ValueError", "foo", "bar")

    def wrong_status(*_, **__):
        ret = type("", (), {})()
        ret.status_code = 404
        ret.text = "test"
        return ret

    monkeypatch.setattr(check_funcs, "get", wrong_status)
    with pytest.raises(ValueError):
        run_weathermap_query("status is 404", "foo", "bar")
