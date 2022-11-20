import math

from handler.geo_population import GeoCoordinate


def test_distance():
    StatueofLibertyLoc = GeoCoordinate(40.6892, -74.0444)
    EiffelTowerLoc = GeoCoordinate(48.8583, 2.2945)
    distance = StatueofLibertyLoc.distance_to(EiffelTowerLoc)
    assert distance > 5800 and distance < 6000
    print(f'The distance between Statue of Liberty and EiffelTower is {distance}km')



def test_boundingbox():
    radius = 5
    EiffelTowerLoc = GeoCoordinate(48.8583, 2.2945)
    min_lon, max_lon, min_lat, max_lat = EiffelTowerLoc.get_boundingbox_within_area(radius)
    print('search the population for 50 kilometers around EiffelTowerLoc')
    print(f'the min location is {min_lat},{min_lon}')
    print(f'the max location is {max_lat},{max_lon}')
    assert min_lat>48.4 and min_lat<48.8583
    assert max_lat>48.8583 and max_lat<49.4
    assert min_lon>1.6 and min_lon<2.3
    assert max_lon>2.29 and max_lon<3.1

def test_boundingbox2():
    # find the whole Earth boundingbox..
    radius = 6355*math.pi
    EiffelTowerLoc = GeoCoordinate(48.8583, 2.2945)
    min_lon, max_lon, min_lat, max_lat = EiffelTowerLoc.get_boundingbox_within_area(radius)
    print('search the population for 50 kilometers around EiffelTowerLoc')
    print(f'the min location is {min_lat},{min_lon}')
    print(f'the max location is {max_lat},{max_lon}')
    print(EiffelTowerLoc.get_boundingbox_within_area(radius))
    assert min_lat==-90
    assert max_lat==90
    assert min_lon==-180
    assert max_lon==180