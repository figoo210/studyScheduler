from database import db
from utils.enums.WeekDay import WeekDay, WeekDayEnum


class Section(db.Model):
    """
    argument of relationship must be capital like class name
    backref can be small because of the model
    laze prefare to be T
    in relations
    one :make db.relation and add column name s like courses
    many: make or put Foreign key on it and name single _id
    Foreign_key=can be small like ("instructor_time.id")

    """
    course_id = db.Column(db.Integer, db.ForeignKey(
        "course.id"), primary_key=True, nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey(
        "instructor.id"), primary_key=True, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey(
        "room.id"), primary_key=True, nullable=True)
    start_time = db.Column(db.String(5), primary_key=True, nullable=True)
    day_of_week = db.Column(WeekDayEnum(
        WeekDay), primary_key=True, nullable=True)
    name = db.Column(db.String(60), unique=False, nullable=False, nullable=True)
    absent = db.Column(db.Boolean, nullable=True)
