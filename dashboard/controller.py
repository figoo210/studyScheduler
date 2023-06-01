from instructor.model import Instructor
from instructor_role.model import InstructorRole
from department.model import Department
from course.model import Course
from room.model import Room
from lecture.model import Lecture
from utils.date_and_time import get_day_name


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


