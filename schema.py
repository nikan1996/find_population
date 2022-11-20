from pprint import pprint

from marshmallow import Schema, fields, ValidationError,validate
class GeoRangeSchema(Schema):
    longitude = fields.Float(validate=validate.Range(min=-180, max=180)) # Degree from -180° ~ 180°
    latitude = fields.Float(validate=validate.Range(min=-90, max=90)) # Degree from -90° ~ 90°
    radius = fields.Float(validate=validate.Range(min=0, max=6378.1))  # Kilometers from  0km ~ 6378.1km (the radius of Earth)


if __name__ == '__main__':
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
        {"longitude": 165, "latitude": 85,"radius":6378.1},
        {"longitude": 165, "latitude": 85,"radius":-1},
        {"longitude": 165, "latitude": 85,"radius":6378.2},
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
        assert str(err) == "{3: {'radius': ['Must be greater than or equal to 0 and less than or equal to 6378.1.']}, 4: {'radius': ['Must be greater than or equal to 0 and less than or equal to 6378.1.']}}"
        print(err.messages)
        # pprint(err.messages)