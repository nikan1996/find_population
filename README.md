# Assignment Requirement
Design and implement a web API in Python to find the population living within an area.

# How do I implement it?
Now I've implemented a simple web API, but the population size will be returned randomly.

Two endpoints:

1. /api/v1/mock/pop_in_area: Return random population.

2. /api/v1/pop_in_area: Return real population. (Now the data are generated randomly)

## Next plan

- [X] Download high precision geo-population data.
- [X] Parse these data and store them into database such as sqlite, redis or other products.
- [X] Find the population within an area.
- [ ] Try Geohash/Google s2 to encode spherical geometry.


# Dev
```shell
pip install -r requirements.txt
flask --app api run
```

# Test
```shell
# There are some unit tests to confirm everything is fine. Type `pytest` to pass all tests.
pytest
```

# Deploy

# Reference
https://halfrost.com/go_spatial_search/

https://ghsl.jrc.ec.europa.eu/documents/GHSL_Data_Package_2022.pdf

https://redis.io/commands/geosearch/

http://janmatuschek.de/LatitudeLongitudeBoundingCoordinates


