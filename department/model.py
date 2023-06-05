from database import db
from sqlalchemy.dialects.mssql import TINYINT, SMALLINT
from utils.enums.Year import Division as Division_Enum
from utils.enums.Year import DivisionEnum

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)
    courses = db.relationship('Course', backref='department_courses', lazy=True)

    def create_general_department_if_not_exist():
        if not Department.query.filter_by(name="عام").first():
            dep = Department(name="عام")
            db.session.add(dep)
            db.session.commit()

# ِAdd Division departments taple
class DivisionDepartments(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    division = db.Column(DivisionEnum(Division_Enum), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    students_count = db.Column(db.Integer, default=0, nullable=True)

    def create_general_division_if_not_exist():
        if not DivisionDepartments.query.filter_by(division=Division_Enum.first).first():
            dd = DivisionDepartments(division=Division_Enum.first, department_id=1)
            db.session.add(dd)

        if not DivisionDepartments.query.filter_by(division=Division_Enum.second).first():
            dd2 = DivisionDepartments(division=Division_Enum.second, department_id=1)
            db.session.add(dd2)

        db.session.commit()
