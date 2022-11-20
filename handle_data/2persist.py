import random
import sqlite3

from tqdm import tqdm

from api import app, db
from models import PopulationRecord


def create_db_table(drop=True):
    try:
        with app.app_context():
            if drop:
                db.drop_all()
            db.create_all()
    except:
        pass


def persist_xyz_data_to_sqlite():
    # Put all the population density data into the sqlite database

    create_db_table()
    filename = 'GHS_POP_E2015_GLOBE_R2019A_4326_30ss_V1_0.xyz'
    count = 0
    with app.app_context():
        with open(filename) as f:
            for line in tqdm(f):
                fields = line.split(' ')
                longitude = float(fields[0])
                latitude = float(fields[1])
                population = float(fields[2])
                record = PopulationRecord(
                    longitude=longitude,
                    latitude=latitude,
                    population=population
                )
                db.session.add(record)
                count+=1
                # flush the pending changes when session has 3000
                if count%3000 ==0:
                    db.session.commit()
    db.session.commit()
def persist_xyz_data_to_sqlite_mock():
    # Put all the population density data into the sqlite database

    create_db_table()
    import numpy as np
    sample_numbers = int(90/0.022)
    print(sample_numbers)
    all_latitudes = np.linspace(-90, 90, num=sample_numbers)
    print(all_latitudes)
    all_longitudes = np.linspace(-180, 180, num=sample_numbers)
    with app.app_context():
        for latitude in  tqdm(all_latitudes):
            for longitude in all_longitudes:
                population = random.randint(0, 10000)
                record = PopulationRecord(
                                    longitude=longitude,
                                    latitude=latitude,
                                    population=population
                                )
                db.session.add(record)
            db.session.commit()
if __name__ == '__main__':
    # persist_xyz_data_to_sqlite()
    persist_xyz_data_to_sqlite_mock()