from instructor.model import Instructor
from instructor_role.model import InstructorRole
from instructor_time.model import InstructorTime
from department.model import Department
from lecture.model import Lecture

from database import db

def get_instructors_data():
    instructors = Instructor.query.all()
    instructors_data = []
    for instructor in instructors:
        instructor_data = {}
        instructor_data['id'] = instructor.id
        instructor_data['name'] = instructor.name
        instructor_data['secuirty_code'] = instructor.secuirty_code
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
    instructor_data['secuirty_code'] = instructor.secuirty_code
    instructor_data['date_of_birth'] = instructor.date_of_birth
    instructor_data['work_years'] = instructor.work_years
    instructor_data['department'] = Department.query.get(instructor.department_id).name
    instructor_data['role'] = instructor.instructor_role
    instructor_data['instructor_times'] = instructor.instructor_times
    instructor_data['instructor_courses'] = instructor.instructor_courses

    return instructor_data


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


