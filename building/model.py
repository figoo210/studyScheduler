from database import db


class Building(db.Model):
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
    name = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)
    rooms = db.relationship("Room", backref="building_rooms", lazy=True)
