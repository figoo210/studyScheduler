from flask import flash
from course.model import Course
from department.model import Department
from regulation.model import Regulation
from database import db
from utils.enums.Semester import Semester, get_translated_semesters


def get_all_courses():
    return Course.query.all()


def get_all_courses_general():
    courses = []
    for c in Course.query.all():
        course = {}
        course["id"] = c.id
        course["name"] = c.name
        course["code"] = c.code
        course["credit_hrs"] = c.credit_hrs
        course["program"] = str(c.program)
        course["reverse_semester"] = c.reverse_semester
        if c.has_section:
            course["has_section"] = 1
        else:
            course["has_section"] = 0
        course["semester"] = str(c.semester)
        course["regulation_id"] = c.regulation_id
        course["regulation"] = Regulation.query.get(c.regulation_id).name
        course["year"] = c.year
        course['department_id'] = c.department_id
        course['department'] = Department.query.get(c.department_id).name
        courses.append(course)
    return courses


# Update Coursse by id
def update_course(course_id, course_name, course_code, credit_hrs, has_section, course_regulation, course_department):
    course = Course.query.get(course_id)
    course.name = course_name
    course.code = course_code
    course.credit_hrs = credit_hrs
    course.has_section = has_section
    course.regulation_id = course_regulation
    course.department_id = course_department
    db.session.commit()


# Update reverse semester in course
def update_reverse_semester(course_id, reverse_semester):
    course = Course.query.get(course_id)
    course.reverse_semester = reverse_semester
    db.session.commit()



# Create Course
def create_course(course_name, course_code, credit_hrs, course_semester,
                  course_year, course_program, has_section,
                  course_regulation, course_department):
    course = Course(name=course_name, code=course_code, credit_hrs=credit_hrs,
                    semester=course_semester, year=course_year,
                    program=course_program, has_section=has_section,
                    regulation_id=course_regulation, department_id=course_department)
    db.session.add(course)
    db.session.commit()
    return course


# Get Course by id
def get_course(course_id):
    course = Course.query.get(course_id)
    return course


# Delete Course by id
def delete_course_by_id(course_id):
    course = Course.query.get(course_id)
    db.session.delete(course)
    db.session.commit()

