import json
from http.client import HTTPException

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError

from handler.geo_population import get_population_within_area, get_population_within_area_mock

from schema import GeoRangeSchema

app = Flask(__name__)
# Load config by namespace
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy()
# Persist all population data into sqlite
db.init_app(app)


# @app.errorhandler(404)
# def endpoint_not_found(error):
#     return "404 not found"
# @app.errorhandler(HTTPException)
# def handle_exception(e):
#     # replace the body with JSON
#     response.data = json.dumps({
#         "code": e.code,
#         "name": e.name,
#         "description": e.description,
#     })
#     response.content_type = "application/json"
#     return response

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/v1/pop_in_area", methods=['GET'])
def pop_in_area_v1():
    """
    get population using
    :return:
    """
    # parameter validation
    try:
        longitude = request.args.get('longitude')
        latitude = request.args.get('latitude')
        radius = request.args.get('radius')
        required_data = {
            "longitude": longitude,
            "latitude": latitude,
            "radius": radius,
        }
        GeoRangeSchema().load(required_data)
        population = get_population_within_area_mock(longitude,latitude,radius)
        return jsonify({
            'population': population,
        })
    except ValidationError as err:
        error_message = str(err)
        return jsonify({
            'error_msg': error_message
        })
    except Exception as e:
        error_message = str(e)
        return jsonify({
            'error_msg': error_message
        })
    return "null"


@app.route("/api/v2/pop_in_area", methods=['GET'])
def pop_in_area_v2():
    """
    using google s2 to expand Earth
    :return:
    """
    return "12345"
