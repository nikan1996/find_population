from marshmallow import ValidationError

from schema import GeoRangeSchema


def test_geo_range_schema():
    geo_range_data1 = [
        {"longitude": 165, "latitude": 85,"radius":50},
        {"longitude": 180, "latitude": 85, "radius": 50},
        {"longitude": -180, "latitude": 85, "radius": 50},
        {"longitude": 181, "latitude": 85,"radius":50},
        {"longitude": -181, "latitude": 85,"radius":50},

    ]
    geo_range_data2 = [
        {"longitude": 165, "latitude": 85,"radius":50},
        {"longitude": 165, "latitude": 90, "radius": 50},
        {"longitude": 165, "latitude": -90, "radius": 50},
        {"longitude": 165, "latitude": -91,"radius":50},
        {"longitude": 165, "latitude": 91,"radius":50},
    ]
    geo_range_data3 = [
        {"longitude": 165, "latitude": 85,"radius":50},
        {"longitude": 165, "latitude": 85,"radius":0},
        {"longitude": 165, "latitude": 85,"radius":10000},
        {"longitude": 165, "latitude": 85,"radius":-1},
        {"longitude": 165, "latitude": 85,"radius":100001},
    ]
    try:
        GeoRangeSchema(many=True).load(geo_range_data1)

    except ValidationError as err:
        print(err.messages)
        assert str(err)== "{3: {'longitude': ['Must be greater than or equal to -180 and less than or equal to 180.']}, 4: {'longitude': ['Must be greater than or equal to -180 and less than or equal to 180.']}}"
        # pprint(err.messages)

    try:
        GeoRangeSchema(many=True).load(geo_range_data2)

    except ValidationError as err:
        assert str(err) == "{3: {'latitude': ['Must be greater than or equal to -90 and less than or equal to 90.']}, 4: {'latitude': ['Must be greater than or equal to -90 and less than or equal to 90.']}}"
        print(err.messages)
        # pprint(err.messages)
    try:
        GeoRangeSchema(many=True).load(geo_range_data3)

    except ValidationError as err:
        assert str(err) == "{3: {'radius': ['Must be greater than or equal to 0 and less than or equal to 10000.']}, 4: {'radius': ['Must be greater than or equal to 0 and less than or equal to 10000.']}}"
        print(err.messages)