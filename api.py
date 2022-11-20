import sys
import traceback

from loguru import logger

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError

from handler.geo_population import get_population_within_area, get_population_within_area_mock

from schema import GeoRangeSchema

# logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")
app = Flask(__name__)
# Load config by namespace
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy()
# Persist all population data into sqlite
db.init_app(app)


# @app.errorhandler(404)
# def endpoint_not_found(error):
#     return "404 not found"

# @app.errorhandler(Exception)
# def handle_exception(e):
#     # pass through HTTP errors
#     if isinstance(e, HTTPException):
#         return e
#
#     # now you're handling non-HTTP exceptions only
#     return “500error handler”, 500

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/v1/mock/pop_in_area", methods=['GET'])
def pop_in_area_mock1():
    """
    get population by location and radius
    :return:
    """
    # parameter validation
    try:
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        radius = request.args.get('radius')
        required_data = {
            "latitude": latitude,
            "longitude": longitude,
            "radius": radius,
        }
        GeoRangeSchema().load(required_data)
        population = get_population_within_area_mock(float(latitude),float(longitude), float(radius))
        logger.info(f'Accept request:{request.full_path}, population result:{population}')
        return jsonify({
            'population': population,
        })
    except Exception as e:
        error_message = str(e)
        logger.error(f'Error in request:{request.full_path},msg:{error_message}')
        return jsonify({
            'error_msg': error_message
        })
@app.route("/api/v1/pop_in_area", methods=['GET'])
def pop_in_area_v1():
    """
    get population by location and radius
    :return:
    """
    # parameter validation
    try:
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        radius = request.args.get('radius')
        required_data = {
            "latitude": latitude,
            "longitude": longitude,
            "radius": radius,
        }
        GeoRangeSchema().load(required_data)
        population = get_population_within_area_mock(float(latitude),float(longitude), float(radius))
        logger.info(f'Accept request:{request.full_path}, population result:{population}')
        return jsonify({
            'population': population,
        })
    except Exception as e:
        error_message = str(e)
        print(traceback.format_exc())
        logger.error(f'Error in request:{request.full_path},msg:{error_message}')
        return jsonify({
            'error_msg': error_message
        })

@app.route("/api/v2/pop_in_area", methods=['GET'])
def pop_in_area_v2():
    """
    More ideas to search population in a specific area
    1. using geohash to encode location.
    2. using google s2 to encode location.
    """
    return {
        'population': 123456,
    }
