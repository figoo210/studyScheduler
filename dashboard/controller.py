import datetime

from flask import flash
from database import db
from dashboard.model import SemesterSettings
from instructor.model import Instructor
from instructor_role.model import InstructorRole
from department.model import Department
from course.model import Course
from room.model import Room
from lecture.model import Lecture
from utils.date_and_time import get_day_name, get_date_from_string
from utils.enums.Semester import Semester, get_translated_semesters

# Get Instructors count
def get_instructors_count():
    return Instructor.query.count()

# Get Courses count
def get_courses_count():
    return Course.query.count()

# Get Rooms count
def get_rooms_count():
    return Room.query.count()

# Get today Lectures count
def get_lectures_count():
    return Lecture.query.filter(Lecture.day_of_week == get_day_name()).count()

# Get sample of instructors in list
def get_instructors_sample(n):
    instructors = Instructor.query.limit(n).all()
    instructors_data = []
    for instructor in instructors:
        data = {
            "first_name": instructor.name,
            "last_name": instructor.name,
            "role": InstructorRole.query.get(instructor.instructor_role).name,
            "department": Department.query.get(instructor.department_id).name,
        }
        instructors_data.append(data)
    return instructors_data

# Get last row of settings table
def get_semesters_from_settings():
    return SemesterSettings.query.order_by(SemesterSettings.id.desc()).first()

# Get Semesters dictionary
def get_semesters_dict():
    semesters = {
        Semester.first: "الأول (الخريف)",
        Semester.second: "الثاني (الربيع)",
        Semester.summer: "الصيفي"
    }
    return semesters

def get_semesters_list():
    semesters = [
        "الأول",
        "الثاني",
        "الصيفي"
    ]
    return semesters

# add new semester settings
def add_semester_settings(data):
    try:
        ss = SemesterSettings(
            semester=data["semester"],
            semester_start_date=get_date_from_string(data["semesterStartAt"]),
            semester_end_date=get_date_from_string(data["semesterEndAt"])
        )
        db.session.add(ss)
        db.session.commit()
        flash("تم تحديث الإعدادات", "success")
    except Exception as e:
        print(e)


def get_current_semester():
    ss = SemesterSettings.query.order_by(SemesterSettings.id.desc()).first()
    data = {
        "id": ss.id,
        "semester": ss.semester,
        "translated_semester": get_translated_semesters()[ss.semester],
        "start_date": ss.semester_start_date,
        "end_date": ss.semester_end_date
    }
    return data
