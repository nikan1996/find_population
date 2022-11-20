from __future__ import annotations

import math
import random


arccos = math.acos
arcsin = math.asin
sin = math.sin
cos = math.cos
radians = math.radians


class GeoCoordinate:
    MIN_LAT = -90
    MAX_LAT = 90
    MIN_LON = -180
    MAX_LON = 180
    EARTH_RADIUS = 6378.1  # kilometers

    def __init__(self, longitude: float, latitude: float):
        self.longitude = radians(longitude)
        self.latitude = radians(latitude)

    def distance_to(self, another: GeoCoordinate):
        # return Great-circle distance
        # https://en.wikipedia.org/wiki/Great-circle_distance
        # dist = arccos(sin(lat1) · sin(lat2) + cos(lat1) · cos(lat2) · cos(lon1 - lon2)) · R
        delta_ = arccos(
            sin(self.latitude) * sin(another.latitude) + cos(self.latitude) * cos(another.latitude) * cos(
                self.longitude - another.longitude))
        distance = delta_ * self.EARTH_RADIUS
        return distance

    def get_boundingbox_within_area(self, radius):
        """
        :param radius:
        :return:
        """
        rad_radius = radius / self.EARTH_RADIUS  # angular radius
        min_lat = self.latitude - rad_radius
        max_lat = self.latitude + rad_radius

        # Δlon = arcsin(sin(r)/cos(lat))
        if min_lat > self.MIN_LAT and max_lat < self.MIN_LAT:
            delta_lon = arcsin((sin(rad_radius) / cos(self.latitude)))
            min_lon = self.longitude - delta_lon
            max_lon = self.longitude + delta_lon
            if min_lon < self.MIN_LON: min_lon += 2 * math.pi
            if max_lon > self.MAX_LON:
                max_lon -= 2 * math.pi
        else:
            min_lat = max(min_lat, self.MIN_LAT)
            max_lat = max(max_lat, self.MIN_LAT)
            min_lon = self.MIN_LON
            max_lon = self.MAX_LON
        return min_lon,max_lon,min_lat,max_lat

def get_population_within_area_mock(longitude, latitude, radius):
    """
    :param longitude:
    :param latitude:
    :param radius:
    :return: population size
    """
    return random.randint(0, 100000)
def get_population_within_area(longitude, latitude, radius):
    """
    :param longitude:
    :param latitude:
    :param radius:
    :return: population size
    """
    return random.randint(0, 100000)
    # location = GeoCoordinate(longitude,latitude)
    # min_lon,max_lon,min_lat,max_lat = location.get_boundingbox_within_area(radius)
    # with app.app_context():



