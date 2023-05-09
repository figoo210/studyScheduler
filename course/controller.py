from course.model import Course


def get_all_courses():
    return Course.query.all()
