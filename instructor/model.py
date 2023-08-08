from database import db
from sqlalchemy.orm import backref
from sqlalchemy.ext.hybrid import hybrid_property


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
    mac_address = db.Column(db.String(48), unique=True, nullable=True)
    date_of_birth = db.Column(db.String(10), unique=False, nullable=True)
    work_years = db.Column(db.Integer, unique=False, nullable=True)

    department_id = db.Column(db.Integer, db.ForeignKey("department.id"), nullable=False)
    instructor_role = db.Column(db.String(20), db.ForeignKey("instructor_role.name"), nullable=False)

    instructor_times = db.relationship("InstructorTime", backref=backref("instructor_time"), lazy=True)
    instructor_courses = db.relationship("InstructorCourse", backref=backref("instructor_course"), lazy=True)
