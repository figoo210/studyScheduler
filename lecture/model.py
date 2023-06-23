from database import db
from utils.enums.WeekDay import WeekDay, WeekDayEnum
from utils.enums.Language import Language, LanguageEnum


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
    # Composite Primary Key
    instructor_course_id = db.Column(db.Integer, db.ForeignKey("instructor_course.id"), primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"), primary_key=True)
    day_of_week = db.Column(WeekDayEnum(WeekDay), primary_key=True)
    start_time = db.Column(db.String(5), primary_key=True)

    group_num = db.Column(db.Integer, unique=False)
    language = db.Column(LanguageEnum(Language), default=Language.ar, nullable=False)
    absent = db.Column(db.Boolean)
    is_section = db.Column(db.Boolean)

    dashboard_id = db.Column(db.Integer, db.ForeignKey('semester_settings.id'), nullable=False)

