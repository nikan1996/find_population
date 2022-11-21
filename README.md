Find the population living within an area.

# How do I implement it?
I've implemented a simple web API, but the population size will be returned randomly.

There are two endpoints:

1. /api/v1/mock/pop_in_area: Return random population.

2. /api/v1/pop_in_area: Return real population. (Now the data are generated randomly)

## Next plan

- [X] Download high precision geo-population data.
- [X] Parse these data and store them into database such as sqlite, redis or other products (Now the data in database are generated randomly because the real data is too large > 200GB).
- [X] Find the population within an area.
- [ ] Dealing with Poles and the meridian at 180° longitude.
- [ ] Try Geohash/Google s2 to encode spherical geometry.



# Dev
```shell
pip install -r requirements.txt
# Generate some data and write them into sqlite. This operation takes about 15minutes.
python -m handle_data.2persist
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


