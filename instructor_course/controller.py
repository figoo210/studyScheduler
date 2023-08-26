from instructor.controller import get_instructor_data
from instructor_course.model import InstructorCourse
from database import db

# Add new Instructor Course
def add_new_instructor_course(instructor_id, course_id, groups_num):
    instructor_course = InstructorCourse(instructor_id=instructor_id, course_id=course_id, groups_num=groups_num)
    db.session.add(instructor_course)
    db.session.commit()
    return instructor_course


# Get all Instructor Courses
def get_all_instructor_courses():
    return InstructorCourse.query.all()

# Get Instructor Course by ID
def get_instructor_course_by_id(id):
    return InstructorCourse.query.get(id)

# Delete Instructor Course by ID
def delete_instructor_course_by_id(id):
    instructor_course = InstructorCourse.query.get(id)
    db.session.delete(instructor_course)
    db.session.commit()

# Update Instructor Course by ID
def update_instructor_course_by_id(id, instructor_id, course_id, groups_num):
    instructor_course = InstructorCourse.query.get(id)
    instructor_course.instructor_id = instructor_id
    instructor_course.course_id = course_id
    instructor_course.groups_num = groups_num
    db.session.commit()


# Get all course instructors
def get_all_course_instructors(course_id):
    cis = InstructorCourse.query.filter_by(course_id=course_id).all()
    result = []
    for ci in cis:
        result.append({
            "instructor_name": get_instructor_data(ci.instructor_id)["name"],
            "groups_num": ci.groups_num
        })
    return result
