import sqlite3

from tqdm import tqdm

from api import app, db
from models import PopulationRecord


def create_db_table():
    try:
        with app.app_context():
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
                population_density = float(fields[2])
                record = PopulationRecord(
                    longitude=longitude,
                    latitude=latitude,
                    population_density=population_density
                )
                db.session.add(record)
                count+=1
                # flush the pending changes when session has 3000
                if count%3000 ==0:
                    db.session.commit()
    db.session.commit()


if __name__ == '__main__':
    persist_xyz_data_to_sqlite()
