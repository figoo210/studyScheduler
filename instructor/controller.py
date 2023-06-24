from instructor.model import Instructor
from instructor_course.model import InstructorCourse
from instructor_role.model import InstructorRole
from instructor_time.model import InstructorTime
from department.model import Department
from lecture.model import Lecture
import hashlib

from database import db, model_to_dict

def get_string_hash(s, length=5):
    sc = hashlib.shake_256(s.encode("utf-8")).hexdigest(length=length)
    return sc

def get_instructors_data():
    instructors = Instructor.query.all()
    instructors_data = []
    for instructor in instructors:
        instructor_data = {}
        instructor_data['id'] = instructor.id
        instructor_data['name'] = instructor.name
        instructor_data['secuirty_code'] = get_string_hash(str(instructor.name) + "-from-" + str(instructor.mac_address or "mac-default"))
        instructor_data['date_of_birth'] = instructor.date_of_birth
        instructor_data['work_years'] = instructor.work_years
        instructor_data['department'] = Department.query.get(instructor.department_id).name
        instructor_data['role'] = instructor.instructor_role
        instructors_data.append(instructor_data)

    return instructors_data

def get_instructors_name():
    instructors = Instructor.query.all()
    instructors_data = []
    for instructor in instructors:
        instructors_data.append(instructor.name)
    return instructors_data

def get_instructor_data(instructor_id):
    instructor = Instructor.query.get(instructor_id)
    instructor_data = {}
    instructor_data['id'] = instructor.id
    instructor_data['name'] = instructor.name
    instructor_data['secuirty_code'] = get_string_hash(str(instructor.name) + "-from-" + str(instructor.mac_address or "mac-default"))
    instructor_data['date_of_birth'] = instructor.date_of_birth
    instructor_data['work_years'] = instructor.work_years
    instructor_data['department'] = Department.query.get(instructor.department_id).name
    instructor_data['department_id'] = instructor.department_id
    instructor_data['role'] = instructor.instructor_role

    instructor_data['instructor_times'] = [model_to_dict(x) for x in instructor.instructor_times]

    instructor_data['instructor_courses'] = [model_to_dict(x) for x in instructor.instructor_courses]

    return instructor_data


def get_filtered_instructors(department_id):
    instructors = []
    for c in Instructor.query.filter_by(department_id=department_id).all():
        cdict = {
            "instructor": model_to_dict(c),
            "instructor_courses": [],
            "instructor_times": []
        }
        for ci in c.instructor_courses:
            cdict["instructor_courses"].append(model_to_dict(ci))
        for ci in c.instructor_times:
            cdict["instructor_times"].append(model_to_dict(ci))
        instructors.append(cdict)
    return instructors


def delete_instructor(instructor_id):
    instructor = Instructor.query.get(instructor_id)
    db.session.delete(instructor)
    db.session.commit()

def add_new_instructor(data):
    instructor = Instructor(
        name=data['name'],
        work_years=data['work_years'],
        department_id=data['department_id'],
        instructor_role=data['role_id']
    )
    db.session.add(instructor)
    db.session.commit()


