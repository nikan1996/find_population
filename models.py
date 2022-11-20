from api import db


class PopulationRecord(db.Model):
    longitude = db.Column(db.Float, nullable=False, primary_key=True)
    latitude = db.Column(db.Float, nullable=False, primary_key=True)
    population_density = db.Column(db.Float,nullable=False)