from datetime import datetime, timedelta
from flask import flash
from dashboard.model import SemesterSettings
from database import db, model_to_dict
from department.model import Department

from lecture.model import Lecture, LectureAttendance
from instructor_course.model import InstructorCourse
from sqlalchemy import func

from course.controller import get_course, get_credit_hrs, get_filtered_courses
from instructor.controller import get_filtered_instructors, get_instructor_data
from dashboard.controller import get_current_semester
from instructor_course.controller import get_instructor_course_by_id
from room.controller import get_all_rooms, get_room_by_id
from building.controller import get_buildings
from utils.date_and_time import add_time_hours, delete_time_minutes, get_date_from_string, get_day_name, get_day_name_from_string_date, get_day_of_week_dates
from utils.enums.WeekDay import get_translated_weekdays
from utils.enums.Language import get_translated_languages
from utils.enums.Program import get_translated_programs
from utils.enums.Year import get_translated_divisions


def lectures_attendance():
    results = []
    curr_semester = get_current_semester()
    for l in get_lectures():
        if l["dashboard_id"] == curr_semester["id"]:
            if not LectureAttendance.query.filter_by(lecture_path=l["path"]).first():
                dates = get_day_of_week_dates(curr_semester["start_date"], curr_semester["end_date"], l["day_of_week"])
                for d in dates:
                    la = LectureAttendance(
                        lecture = l["course"]["name"],
                        lecture_path = l["path"],
                        day_of_week = l["day_of_week"],
                        date = d,
                        attended = False,
                        replacement = False,
                        online = False,
                    )
                    db.session.add(la)
                    db.session.commit()
    for la in LectureAttendance.query.group_by(LectureAttendance.lecture_path).all():
        if "-" in la.lecture_path:
            if not Lecture.query.filter_by(path=la.lecture_path).first():
                LectureAttendance.query.filter(LectureAttendance.lecture_path == la.lecture_path).delete()
                db.session.commit()
                print("DELETED: ", la.lecture_path)



def overwrite_group_table(data):
    curr_semester = get_current_semester()
    pdl = data["path"].split("-")
    group_path_checker = f"{pdl[0]}-{pdl[1]}-{pdl[2]}-{pdl[3]}-{pdl[4]}"
    group_path = f"{pdl[0]}-{pdl[1]}-{pdl[2]}-{pdl[3]}-{pdl[4]}-{pdl[7]}"
    for t in Lecture.query.filter(Lecture.path.ilike(f'%{group_path_checker}%'), Lecture.dashboard_id==curr_semester["id"]).all():
        cpdl = t.path.split("-")
        current_group_path = f"{cpdl[0]}-{cpdl[1]}-{cpdl[2]}-{cpdl[3]}-{cpdl[4]}-{cpdl[7]}"
        if group_path == current_group_path:
            # delete this lecture
            db.session.delete(t)
            db.session.commit()


def get_groups_num(path_base, year):
    curr_semester = get_current_semester()
    counter = 0
    while True:
        lecture = Lecture.query.filter(Lecture.path.ilike(f'%{path_base}-{counter}%{year}'), Lecture.dashboard_id==curr_semester["id"]).first()
        if lecture:
            counter = counter + 1
        else:
            break
    return counter


def read_lecture_path(path):
    pdl = path.split("-")
    path_base = f"{pdl[0]}-{pdl[1]}-{pdl[2]}-{pdl[3]}"
    trans_program = ""
    if pdl[1] != "NoProgram":
        trans_program = get_translated_programs()[pdl[1]]
    return {
        "language": pdl[0],
        "language_trans": get_translated_languages()[pdl[0]],
        "program": pdl[1],
        "program_trans": trans_program,
        "department_id": pdl[2],
        "department": Department.query.get(pdl[2]).name,
        "group_num": int(pdl[4]),
        "day": pdl[5],
        "day_trans": get_translated_weekdays()[pdl[5]],
        "lecture_num": pdl[6],
        "year": pdl[7],
        "year_trans": get_translated_divisions()[pdl[7]],
        "no_of_groups": get_groups_num(path_base, pdl[7])
    }


def dont_save_for_similarity(instructor_course_id, data, current_dashboard_id):
    pdl = data["path"].split("-")
    group_path = f"{pdl[0]}-{pdl[1]}-{pdl[2]}-{pdl[3]}-{pdl[4]}-{pdl[7]}"
    for t in Lecture.query.filter_by(
        instructor_course_id=instructor_course_id,
        room_id=data['room'],
        start_time=data['startTime'],
        day_of_week=data['day'],
        dashboard_id=current_dashboard_id
    ).all():
        cpdl = t.path.split("-")
        current_group_path = f"{cpdl[0]}-{cpdl[1]}-{cpdl[2]}-{cpdl[3]}-{cpdl[4]}-{cpdl[7]}"

        if group_path == current_group_path:
            return True, t.path

    return False, None


def is_lectures_time_intersect(start1, end1, start2, end2):
    if start1 <= start2 <= end1 or \
        start1 <= end2 <= end1 or \
        start2 <= start1 <= end2 or \
        start2 <= end1 <= end2:
        return True
    else:
        return False


def is_room_available(room, day, start_time, credit_hrs):
    curr_semester = get_current_semester()

    start1 = datetime.strptime(start_time, "%H:%M").time()
    end1 = delete_time_minutes(add_time_hours(start1, int(credit_hrs)), 1)

    # Find all lecture rooms in this day
    for lecture in Lecture.query.filter_by(room_id=room, day_of_week=day, dashboard_id=curr_semester["id"]).all():
        # Check time
        start2= datetime.strptime(lecture.start_time, "%H:%M").time()
        course_id = InstructorCourse.query.get(lecture.instructor_course_id).course_id
        end2 = delete_time_minutes(add_time_hours(start2, get_credit_hrs(course_id)), 1)
        if is_lectures_time_intersect(start1, end1, start2, end2):
            return False, lecture.path
    return True, None


def is_instructor_available(instructor, day, start_time, credit_hrs):
    curr_semester = get_current_semester()

    start1 = datetime.strptime(start_time, "%H:%M").time()
    end1 = delete_time_minutes(add_time_hours(start1, int(credit_hrs)), 1)

    for ic in InstructorCourse.query.filter_by(instructor_id=instructor).all():
        for lecture in Lecture.query.filter_by(instructor_course_id=ic.id, day_of_week=day, dashboard_id=curr_semester["id"]).all():
            # Check time
            start2= datetime.strptime(lecture.start_time, "%H:%M").time()
            end2 = delete_time_minutes(add_time_hours(start2, get_credit_hrs(ic.course_id)), 1)
            if is_lectures_time_intersect(start1, end1, start2, end2):
                return False, lecture.path
    return True, None


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

    # Check if all data are similar but in different group save it, else return
    dont_save, path_error = dont_save_for_similarity(instructor_course.id, data, current_dashboard.id)
    if dont_save:
        return "هذة المحاضرة موجودة بالفعل", data["path"], path_error

    # Check room availability
    room_available, prepath = is_room_available(data["room"], data["day"], data["startTime"], get_credit_hrs(data["course"]))
    if not room_available:
        return 'تعارض في المواعيد', data["path"], prepath

    # Check instructor availability
    instructor_available, prepath2 = is_instructor_available(data["instructor"], data["day"], data["startTime"], get_credit_hrs(data["course"]))
    if not instructor_available:
        return 'تعارض في المواعيد', data["path"], prepath2


    lecture = Lecture(
        instructor_course_id=instructor_course.id,
        room_id=data['room'],
        start_time=data['startTime'],
        path=data['path'],
        day_of_week=data['day'],
        group_num=1,
        dashboard_id=current_dashboard.id
    )
    db.session.add(lecture)
    db.session.commit()

    return False, "Done", "No Conflict"


def replacement_lecture(data):
    course_name = get_course(data["course_id"])["name"]
    is_online = False
    if data["place"] == "online":
        is_online = True
    la = LectureAttendance(
        lecture = course_name,
        lecture_path = data["instructorName"],
        day_of_week = get_day_name_from_string_date(data["date"], date_format="%d/%m/%Y"),
        date = get_date_from_string(data["date"], date_format="%d/%m/%Y"),
        attended = True,
        replacement = True,
        online = is_online,
    )
    db.session.add(la)
    db.session.commit()


def lecture_attend(lecture_path, date=datetime.now().date()):
    lecture = LectureAttendance.query.filter_by(lecture_path=lecture_path, date=date).first()
    lecture.attended = True
    db.session.commit()


def lecture_absent(lecture_path, date=datetime.now().date()):
    lecture = LectureAttendance.query.filter_by(lecture_path=lecture_path, date=date).first()
    lecture.attended = False
    db.session.commit()


def get_lectures(attendance_date=None):
    """
    Get all lectures from the database.
    """
    lectures = []
    curr_semester = get_current_semester()

    for le in Lecture.query.filter(Lecture.dashboard_id==curr_semester["id"]).order_by(func.time(Lecture.start_time)).all():
        data = {}
        data["instructor_course_id"] = le.instructor_course_id
        data["instructor_id"] = get_instructor_course_by_id(le.instructor_course_id).instructor_id
        data["instructor"] = get_instructor_data(data["instructor_id"])
        data["course"] = get_course(get_instructor_course_by_id(le.instructor_course_id).course_id)
        data["course_id"] = get_instructor_course_by_id(le.instructor_course_id).course_id
        data["room_id"] = le.room_id
        data["room"] = get_room_by_id(le.room_id)
        data["day_of_week"] = le.day_of_week
        data["start_time"] = le.start_time
        data["end_time"] = add_time_hours(datetime.strptime(le.start_time, "%H:%M").time(), int(data["course"]["credit_hrs"])).strftime("%H:%M")
        data["path"] = le.path
        data["group_num"] = le.group_num
        data["language"] = le.language
        data["attended"] = is_attended(le.path, attendance_date)
        data["is_section"] = le.is_section
        data["dashboard_id"] = le.dashboard_id
        data["dashboard"] = get_current_semester()
        data["current_year"] = f'{str(get_current_semester()["end_date"]).split("-")[0]}/{int(str(get_current_semester()["end_date"]).split("-")[0]) + 1}'
        data["path_data"] = read_lecture_path(le.path)
        lectures.append(data)
    return lectures


def get_today_lectures(date=None):
    lectures = []
    day_name = get_day_name()
    if date:
        day_name = get_day_name_from_string_date(date)
        date = get_date_from_string(date)
    else:
        date = datetime.now().date()
    for l in get_lectures(attendance_date=date):
        if l["day_of_week"] == day_name:
            lectures.append(l)
    return lectures


def is_attended(lp, date=datetime.now().date()):
    la = LectureAttendance.query.filter_by(lecture_path=lp, date=date).first()
    if la:
        if la.attended:
            return True
        else:
            return False
    else:
        return False


def get_instructor_lectures_table(id):
    lectures = []
    for lecture in get_lectures():
        if lecture["instructor_id"] == int(id):
            lectures.append(lecture)
    return lectures


def get_instructor_lectures_statistics(id):
    curr_semester = get_current_semester()

    instructor_lectures = get_instructor_lectures_table(id)
    results = []
    for il in instructor_lectures:
        attendance = 0
        absent = 0
        if il["dashboard_id"] == curr_semester["id"]:
            semester_lectures_num = len(get_day_of_week_dates(curr_semester["start_date"], curr_semester["end_date"], il["day_of_week"]))
            for la in LectureAttendance.query.filter_by(lecture_path=il["path"]).all():
                present = datetime.now()
                if la.date < present.date():
                    if la.attended == True:
                        attendance = attendance + 1
                    else:
                        absent = absent + 1
            results.append({
                "course": il["course"]["name"],
                "semester_lectures_num": semester_lectures_num,
                "attendance": attendance,
                "absent": absent,
                "next_lectures": semester_lectures_num - (attendance + absent),
            })

    return results


def get_course_lectures_table(id):
    lectures = []
    for lecture in get_lectures():
        if lecture["course_id"] == int(id):
            lectures.append(lecture)
    return lectures


def get_lecture_by_path(path):
    for l in get_lectures():
        if path == l['path']:
            return l


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


def get_api_lectures_data(department_id, semester, year, regulation_id, program, table_type):
    data = {
        "lectures": get_lectures(),
        "instructors": get_filtered_instructors(table_type),
        "courses": get_filtered_courses(semester, year, program, regulation_id, department_id, table_type),
        "buildings": get_buildings(),
        "rooms": get_all_rooms(),
    }
    return data
