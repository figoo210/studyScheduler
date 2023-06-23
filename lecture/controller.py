from flask import flash
from database import db

from lecture.model import Lecture
from course.controller import get_course
from dashboard.controller import get_current_semester
from instructor_course.controller import get_instructor_course_by_id

def add_new_lecture(data):
    """
    Add a new lecture to the database.
    """
    lecture = Lecture(course_id=data['course_id'],instructor_id=data['instructor_id'])
    db.session.add(lecture)
    db.session.commit()
    flash("تم اضافة الماده ", "success")

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
        data["course"] = get_course(get_instructor_course_by_id(le.instructor_course_id).course_id)
        data["room_id"] = le.room_id
        data["day_of_week"] = le.day_of_week
        data["start_time"] = le.start_time
        data["group_num"] = le.group_num
        data["language"] = le.language
        data["absent"] = le.absent
        data["is_section"] = le.is_section
        data["dashboard_id"] = le.dashboard_id
        data["dashboard"] = get_current_semester()
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
