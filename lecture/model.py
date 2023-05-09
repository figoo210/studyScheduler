from database import db
from utils.enums.WeekDay import WeekDay, WeekDayEnum


class Lecture(db.Model):
    """
    argument of relationship must be capital like class name 
    backref can be small because of the model
    laze prefare to be T
    in relations 
    one :make db.relation and add column name s like courses  
    many: make or put Foreign key on it and name single _id 
    Foreign_key=can be small like ("instructor_time.id")

    """
    course_id = db.Column(db.Integer, primary_key=True,
                          Foreign_key=("course.id"))
    instructor_id = db.Column(
        db.Integer, primary_key=True, Foreign_key=("instructor.id"))
    room_id = db.Column(db.Integer, primary_key=True, Foreign_key=("room.id"))
    start_time = db.Column(db.String(5), primary_key=True)
    day_of_week = db.Column(WeekDayEnum(WeekDay), primary_key=True)
    name = db.Column(db.String(60), unique=False, nullable=False)
    absent = db.column(db.Boolean, unique=False, nullable=True, default=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)
