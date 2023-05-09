from database import db
from utils.enums.Language import Language, LanguageEnum
from utils.enums.Semester import Semester, SemesterEnum
from utils.enums.Year import Year, YearEnum
from utils.enums.Program import Program, ProgramEnum


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    code = db.Column(db.String(60), unique=True, nullable=False)
    credit_hrs = db.Column(db.Integer, unique=False, nullable=False)
    semester = db.Column(SemesterEnum(Semester),
                         default=Semester.first, nullable=False)
    year = db.Column(YearEnum(Year), default=Year.first, nullable=False)
    language = db.Column(LanguageEnum(Language),
                         default=Language.ar, nullable=False)
    program = db.Column(ProgramEnum(Program),
                        default=Program.regularity, nullable=False)
    has_section = db.Column(db.Boolean)
    regulation_id = db.Column(db.Integer, db.ForeignKey('regulation.id'), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
