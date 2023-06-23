from database import db
from sqlalchemy.orm import backref


class Room(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    qr_code = db.Column(db.Text, unique=True, nullable=True)
    real_capacity = db.Column(db.Integer, unique=False, nullable=True)
    supported_capacity = db.Column(db.Integer, unique=False, nullable=True)

    building_id = db.Column(db.Integer, db.ForeignKey("building.id"))

    lectures = db.relationship('Lecture', backref=backref('room_lectures'), lazy=True)
