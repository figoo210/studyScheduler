from flask import flash
from course.model import Course, CourseUpdates
from department.model import Department
from regulation.model import Regulation
from dashboard.model import SemesterSettings
from database import db, model_to_dict
from utils.enums.Semester import Semester, get_translated_semesters


def get_all_courses():
    return Course.query.all()

def get_filtered_courses(semester, year, program, regulation_id, department_id):
    courses = []
    for c in Course.query.filter_by(semester=semester, year=year, program=program, regulation_id=regulation_id, department_id=department_id).all():
        cdict = {
            "course": model_to_dict(c),
            "course_instructors": []
        }
        for ci in c.instructor_courses:
            cdict["course_instructors"].append(model_to_dict(ci))
        courses.append(cdict)
    return courses


def get_all_courses_general():
    courses = []
    for c in get_all_courses():
        course = {}
        course["id"] = c.id
        course["name"] = c.name
        course["code"] = c.code
        course["credit_hrs"] = c.credit_hrs
        course["program"] = str(c.program)
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
        course['has_summer'] = is_has_summer(c.id)
        course['has_reverse'] = is_has_reverse(c.id)
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
    current_dashboard = SemesterSettings.query.order_by(SemesterSettings.id.desc()).first()
    key = (course_id, current_dashboard.id, Semester.reverse)
    course_update = CourseUpdates.query.get(key)
    if reverse_semester:
        if not course_update:
            new_course_update = CourseUpdates(
                course_id=course_id,
                semester_type=Semester.reverse,
                dashboard_id=current_dashboard.id,
            )
            db.session.add(new_course_update)
            db.session.commit()
    else:
        if course_update:
            db.session.delete(course_update)
            db.session.commit()


# Update summer semester in course
def update_summer_semester(course_id, summer_semester):
    current_dashboard = SemesterSettings.query.order_by(SemesterSettings.id.desc()).first()
    key = (course_id, current_dashboard.id, Semester.summer)
    course_update = CourseUpdates.query.get(key)
    if summer_semester:
        if not course_update:
            new_course_update = CourseUpdates(
                course_id=course_id,
                semester_type=Semester.summer,
                dashboard_id=current_dashboard.id,
            )
            db.session.add(new_course_update)
            db.session.commit()
    else:
        if course_update:
            cutd = db.session.query(CourseUpdates).get(key)
            print("#################################: ", cutd)
            db.session.delete(cutd)
            db.session.commit()


def is_has_summer(course_id):
    current_dashboard = SemesterSettings.query.order_by(SemesterSettings.id.desc()).first()
    key = (course_id, current_dashboard.id, Semester.summer)
    if CourseUpdates.query.get(key):
        return True
    else:
        return False


def is_has_reverse(course_id):
    current_dashboard = SemesterSettings.query.order_by(SemesterSettings.id.desc()).first()
    key = (course_id, current_dashboard.id, Semester.reverse)
    if CourseUpdates.query.get(key):
        return True
    else:
        return False



# Create Course
def create_course(course_name, course_code, credit_hrs, course_semester,
                  course_year, course_program, has_section,
                  course_regulation, course_department):
    course = Course(
        name=course_name,
        code=course_code,
        credit_hrs=credit_hrs,
        semester=course_semester,
        year=course_year,
        program=course_program,
        has_section=has_section,
        regulation_id=course_regulation,
        department_id=course_department,
    )
    db.session.add(course)
    db.session.commit()
    return course


# Get Course by id
def get_course(course_id):
    c = Course.query.get(course_id)
    course = {}
    course["id"] = c.id
    course["name"] = c.name
    course["code"] = c.code
    course["credit_hrs"] = c.credit_hrs
    course["program"] = str(c.program)
    if c.has_section:
        course["has_section"] = 1
    else:
        course["has_section"] = 0
    course["semester"] = str(c.semester)
    course["regulation_id"] = c.regulation_id
    course["regulation"] = Regulation.query.get(c.regulation_id).name
    course["year"] = str(c.year.value)
    course['department_id'] = c.department_id
    course['department'] = Department.query.get(c.department_id).name
    course['has_summer'] = is_has_summer(c.id)
    course['has_reverse'] = is_has_reverse(c.id)
    return course


# Delete Course by id
def delete_course_by_id(course_id):
    course = Course.query.get(course_id)
    db.session.delete(course)
    db.session.commit()

