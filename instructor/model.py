from database import db


class Instructor(db.Model):

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
    mac_address = db.Column(db.Integer, unique=True, nullable=True)
    secuirty_code = db.Column(db.Integer, unique=True, nullable=False)
    health_status = db.Column(db.String(20), unique=False, nullable=True)
    date_of_birth = db.Column(db.DateTime, unique=False, nullable=True)
    date_of_join = db.Column(db.DateTime, unique=False, nullable=True)
    department_id = db.Column(db.Integer, db.ForeignKey(
        "department.id"), nullable=False)
    instructor_role = db.Column(db.String(20), db.ForeignKey(
        "instructor_role.name"), nullable=False)
    lectures = db.relationship("Lecture", backref="lecture", lazy=True)
    sections = db.relationship("Section", backref="section", lazy=True)
    instructor_times = db.relationship("InstructorTime", backref="instructor_time", lazy=True)
