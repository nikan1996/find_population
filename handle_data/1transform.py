from osgeo import gdal

import os

path = r"GHS_POP_E2015_GLOBE_R2019A_4326_30ss_V1_0.tif"

output_path = r'GHS_POP_E2015_GLOBE_R2019A_4326_30ss_V1_0.xyz'
if __name__ == '__main__':

    if os.path.exists(path):
        print('Start transform...')
        ds = gdal.Open(path)

        xyz = gdal.Translate(output_path, ds)
        print('Finished')
    else:
        print('The path is invalid')