from api import db


class PopulationRecord(db.Model):
    latitude = db.Column(db.Float, nullable=False, primary_key=True)
    longitude = db.Column(db.Float, nullable=False, primary_key=True)
    population = db.Column(db.Float,nullable=False)