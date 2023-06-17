from course.model import Course
from department.model import Department


def get_all_courses():
    return Course.query.all()


def get_all_courses_general():
    courses = []
    for c in Course.query.all():
        course = {}
        course["id"] = c.id
        course["name"] = c.name
        course["semester"] = c.semester
        course["regulation"] = c.regulation_id
        course["year"] = c.year
        course['department'] = Department.query.get(c.department_id).name
    return courses









