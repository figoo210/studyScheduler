from database import db
from sqlalchemy.orm import backref
from department.controller import get_department_by_id
from utils.enums.Semester import Semester, SemesterEnum
from utils.enums.Year import Division, DivisionEnum
from utils.enums.Program import Program, ProgramEnum, get_translated_programs


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    code = db.Column(db.String(60), unique=False, nullable=True)
    credit_hrs = db.Column(db.Integer, unique=False, nullable=False)
    semester = db.Column(SemesterEnum(Semester), default=Semester.first, nullable=False)
    year = db.Column(DivisionEnum(Division), default=Division.first, nullable=False)
    program = db.Column(ProgramEnum(Program),
                        default=Program.regularity, nullable=False)
    has_section = db.Column(db.Boolean)

    regulation_id = db.Column(db.Integer, db.ForeignKey('regulation.id'), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)

    course_updates = db.relationship('CourseUpdates', backref=backref('course_update'), lazy=True)
    instructor_courses = db.relationship("InstructorCourse", backref=backref("course_with_instructors"), lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': f"{self.name} ({self.credit_hrs}) {get_department_by_id(self.department_id).name} {get_translated_programs()[self.program]}"
        }



class CourseUpdates(db.Model):
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    dashboard_id = db.Column(db.Integer, db.ForeignKey('semester_settings.id'), primary_key=True)
    semester_type = db.Column(SemesterEnum(Semester), default=Semester.summer, primary_key=True)
