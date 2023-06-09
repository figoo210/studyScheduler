from database import db
from sqlalchemy.orm import backref


class Room(db.Model):
    """
    argument of relationship must be capital like class name
    backref can be small because of the model
    laze prefare to be T
    in relations
    one :make db.relation and add column name s like courses
    many: make or put Foreign key on it and name single _id
    Foreign_key=can be small like ("instructor_time.id")

    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    qr_code = db.Column(db.Text, unique=True, nullable=True)
    real_capacity = db.Column(db.Integer, unique=False, nullable=True)
    supported_capacity = db.Column(db.Integer, unique=False, nullable=True)

    building_id = db.Column(db.Integer, db.ForeignKey("building.id"))

    lectures = db.relationship('Lecture', backref=backref('room_lectures'), lazy=True)
