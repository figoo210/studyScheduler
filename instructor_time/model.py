from database import db
from utils.enums.WeekDay import WeekDay, WeekDayEnum


class InstructorTime(db.Model):
    """
    argument of relationship must be capital like class name
    backref can be small because of the model
    laze prefare to be T
    in relations
    one :make db.relation and add column name s like courses
    many: make or put Foreign key on it and name single (_id)
    Foreign_key=can be small like ("instructor_time.id")
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_time = db.Column(db.String(5), unique=False, nullable=False)
    day_of_week = db.Column(WeekDayEnum(
        WeekDay), default=WeekDay.sat, nullable=False)
    end_time = db.Column(db.String(5), unique=False, nullable=False)
    instructor_id = db.Column(
        db.Integer, db.ForeignKey("instructor.id"), nullable=False)
