from flask import flash
from dashboard.model import SemesterSettings
from database import db

from lecture.model import Lecture
from instructor_course.model import InstructorCourse

from course.controller import get_course, get_filtered_courses
from instructor.controller import get_filtered_instructors, get_instructor_data
from dashboard.controller import get_current_semester
from instructor_course.controller import get_instructor_course_by_id
from room.controller import get_all_rooms
from building.controller import get_buildings

def add_new_lecture(data):
    """
    Add a new lecture to the database.
    """
    # get instructor_course by instructor_id and course_id
    instructor_course = InstructorCourse.query\
        .filter_by(course_id=data['course'], instructor_id=data['instructor'])\
        .order_by(InstructorCourse.id.desc())\
        .first()
    current_dashboard = SemesterSettings.query.order_by(SemesterSettings.id.desc()).first()
    lecture = Lecture(
        instructor_course_id=instructor_course.id,
        room_id=data['room'],
        start_time=data['startTime'],
        day_of_week=data['day'],
        group_num=1,
        dashboard_id=current_dashboard.id
    )
    db.session.add(lecture)
    db.session.commit()
    return lecture

def update_lecture(room_id,start_time,day_of_week,name,absent):

    lecture = Lecture.query.get()
    lecture.room_id = room_id
    lecture.start_time = start_time
    lecture.day_of_week = day_of_week
    lecture.name = name
    lecture.absent = absent
    db.session.commit()

def get_lectures():
    """
    Get all lectures from the database.
    """
    lectures = []
    for le in Lecture.query.all():
        data = {}
        data["instructor_course_id"] = le.instructor_course_id
        data["instructor_id"] = get_instructor_course_by_id(le.instructor_course_id).instructor_id
        data["instructor"] = get_instructor_data(data["instructor_id"])
        data["course"] = get_course(get_instructor_course_by_id(le.instructor_course_id).course_id)
        data["course_id"] = get_instructor_course_by_id(le.instructor_course_id).course_id
        data["room_id"] = le.room_id
        data["day_of_week"] = le.day_of_week
        data["start_time"] = le.start_time
        data["group_num"] = le.group_num
        data["language"] = le.language
        data["absent"] = le.absent
        data["is_section"] = le.is_section
        data["dashboard_id"] = le.dashboard_id
        data["dashboard"] = get_current_semester()
        data["current_year"] = f'{str(get_current_semester()["end_date"]).split("-")[0]}/{int(str(get_current_semester()["end_date"]).split("-")[0]) + 1}'
        lectures.append(data)
    return lectures

def delete_time(bid):
    """
    Delete a Time from the database.
    """
    lecture = Lecture.query.get(bid)
    db.session.delete(lecture)
    db.session.commit()
    flash("تم حذف الماده ", "success")


from flask import flash
def is_form_empty(AuthForm):
    # Loop through all form fields
    for field in AuthForm.values():
        # Check if the field has a value
        if field.strip() != '':
            flash("لم يتم الحفظ")
            return False  # Form is not empty
        flash("تم الحفظ")
    return True  # Form is empty

"""
# To use this function
check = is_form_empty(AuthForm)
# True if form is empty, False otherwise
print(check)

"""

def get_api_lectures_data(department_id, semester, year, regulation_id, program):
    data = {
        "lectures": get_lectures(),
        "instructors": get_filtered_instructors(department_id),
        "courses": get_filtered_courses(semester, year, program, regulation_id, department_id),
        "buildings": get_buildings(),
        "rooms": get_all_rooms(),
    }
    return data
