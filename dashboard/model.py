from database import db
from sqlalchemy.orm import backref
from utils.enums.Semester import Semester, SemesterEnum

# Semester Settings Model
class SemesterSettings(db.Model):
    # Primary Key
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    semester = db.Column(SemesterEnum(Semester), default=Semester.first, nullable=False)
    semester_start_date = db.Column(db.Date, nullable=False)
    semester_end_date = db.Column(db.Date, nullable=False)

    course_dashboards = db.relationship('CourseUpdates', backref=backref('course_dashboard'), lazy=True)
    lecture_dashboards = db.relationship('Lecture', backref=backref('lecture_dashboard'), lazy=True)

