import json
import random

import pytest

from api import app


@pytest.fixture()
def flask_app():
    app.config.update({
        "TESTING": True,
    })
    # setup code

    yield app

    # clean up code


@pytest.fixture()
def client(flask_app):
    return flask_app.test_client()


def test_pop_pop_in_area(client):
    response = client.get("/api/v1/pop_in_area")
    assert "Field may not be null" in response.get_data(as_text=True)

    response = client.get("/api/v1/pop_in_area?longitude=191.3&latitude=31&radius=50")
    assert "Must be greater than or equal to -180 and less than or equal to 180." in response.get_data(as_text=True)

    response = client.get("/api/v1/pop_in_area?longitude=-191.3&latitude=31&radius=50")
    assert "Must be greater than or equal to -180 and less than or equal to 180." in response.get_data(as_text=True)

    response = client.get("/api/v1/pop_in_area?longitude=155&latitude=-91&radius=50")
    assert "Must be greater than or equal to -90 and less than or equal to 90." in response.get_data(as_text=True)

    response = client.get("/api/v1/pop_in_area?longitude=155&latitude=91&radius=50")
    assert "Must be greater than or equal to -90 and less than or equal to 90." in response.get_data(as_text=True)

    response = client.get("/api/v1/pop_in_area?longitude=155&latitude=55&radius=-50")
    assert "Must be greater than or equal to 0 and less than or equal to 10000." in response.get_data(as_text=True)

    response = client.get("/api/v1/pop_in_area?longitude=155&latitude=55&radius=3")
    data = response.get_data(as_text=True)
    json_data = json.loads(data)
    assert json_data["population"] > 0
    print(json_data["population"])
    for i in range(10):
        random_longitude = random.uniform(-180, 180)
        random_latitude = random.uniform(-90, 90)
        random_radius = random.uniform(0, 10000)
        response = client.get(
            f"/api/v1/pop_in_area?longitude={random_longitude}&latitude={random_latitude}&radius={random_radius}")
        data = response.get_data(as_text=True)
        json_data = json.loads(data)
        print(json_data)
        assert json_data["population"] > 0
