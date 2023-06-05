from database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from utils.enums.Semester import Semester, SemesterEnum

# Semester Settings Model
class SemesterSettings(db.Model):
    # Primary Key
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    semester = db.Column(SemesterEnum(Semester), default=Semester.first, nullable=False)
    semester_start_date = db.Column(db.Date, nullable=False)
    semester_end_date = db.Column(db.Date, nullable=False)



