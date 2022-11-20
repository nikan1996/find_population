from osgeo import gdal
rds = gdal.Open(r"C:\Users\kanye\PycharmProjects\terry_assignment\handle_data\GHS_POP_P2030_GLOBE_R2022A_54009_100_V1_0_R11_C13.tif")
print(dir(rds))
print(rds.GetDescription())
print(rds.RasterCount)
print(rds.RasterXSize)
print(rds.RasterYSize)
print(rds.GetProjection()) # World_Mollweide, WGS 84