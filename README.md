# Assignment Requirement
Design and implement a web API in Python to find the population living within an area.

# How I implement it?
Now I've implemented a simple web API, but the population size will be returned randomly.

## Next plan

- [X] Download high precision geo-population data.
- [ ] [Working] Parse these data and store them into database such as sqlite, redis or other products.
- [ ] [Working] Find the population whinin an area.
- [ ] Try Geohash/Google s2 to encode spherical geometry.


# Dev
```shell
pip install -r requirements.txt
flask --app api run
```

# Test
```shell
pytest
```

# Reference
https://halfrost.com/go_spatial_search/

https://ghsl.jrc.ec.europa.eu/documents/GHSL_Data_Package_2022.pdf

https://redis.io/commands/geosearch/

http://janmatuschek.de/LatitudeLongitudeBoundingCoordinates


