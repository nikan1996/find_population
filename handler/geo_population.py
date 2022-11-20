from __future__ import annotations

import math
import random


arccos = math.acos
arcsin = math.asin
sin = math.sin
cos = math.cos
radians = math.radians


class GeoCoordinate:
    MIN_LAT = radians(-90)
    MAX_LAT = radians(90)
    MIN_LON = radians(-180)
    MAX_LON = radians(180)
    EARTH_RADIUS = 6378.1  # kilometers

    def __init__(self,  latitude: float,longitude: float):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

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
        if min_lat > self.MIN_LAT and max_lat < self.MAX_LAT:
            delta_lon = arcsin((sin(rad_radius) / cos(self.latitude)))
            min_lon = self.longitude - delta_lon
            max_lon = self.longitude + delta_lon
            if min_lon < self.MIN_LON:
                min_lon += 2 * math.pi
            if max_lon > self.MAX_LON:
                max_lon -= 2 * math.pi
        else:
            min_lat = max(min_lat, self.MIN_LAT)
            max_lat = min(max_lat, self.MAX_LAT)
            min_lon = self.MIN_LON
            max_lon = self.MAX_LON
        return math.degrees(min_lon),math.degrees(max_lon),math.degrees(min_lat),math.degrees(max_lat)

def get_population_within_area_mock(latitude,longitude, radius):
    """
    :param longitude:
    :param latitude:
    :param radius:
    :return: population size
    """
    return int(random.randint(0, 100000))
def get_population_within_area( latitude,longitude, radius):
    """
    :param longitude:
    :param latitude:
    :param radius:
    :return: population size
    """
    location = GeoCoordinate(latitude,longitude)
    min_lon,max_lon,min_lat,max_lat = location.get_boundingbox_within_area(radius)
    from api import app,db
    population  = 0
    with app.app_context():
        sql = f"SELECT * FROM population_record WHERE (latitude >= {min_lat} AND latitude <= {max_lat}) AND (longitude >= {min_lon} AND longitude <= {max_lon})"
        result = db.engine.execute(sql)
        for r in result:
            population += r[2]
    return int(population)



if __name__ == '__main__':
    population = get_population_within_area(48.8583, 2.2945,radius=500)
    print(population)