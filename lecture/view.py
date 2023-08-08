import json
from flask import Blueprint, redirect, render_template, request
from instructor.controller import get_instructors_data, get_instructors_name
from lecture.controller import add_new_lecture, get_lecture_by_path, get_lectures, get_api_lectures_data, get_today_lectures, lecture_attend, lecture_absent, lectures_attendance, overwrite_group_table, replacement_lecture
from regulation.controller import get_regulations
from department.controller import get_all_divisions_departments
from room.controller import get_all_rooms
from building.controller import get_buildings

from utils.enums.Program import get_translated_programs, Program
from utils.enums.Semester import Semester, get_translated_semesters
from utils.enums.Year import Division, get_translated_divisions
from utils.enums.Language import get_translated_languages
from utils.enums.WeekDay import get_translated_weekdays
from utils.date_and_time import get_date_from_string


PAGE = 'lecture'

bp = Blueprint(PAGE, __name__, template_folder='templates')


@bp.route(f'/{PAGE}/attend/<lecture_path>/<check>', methods=["GET"])
def set_attendance(lecture_path, check):
    """ set_absent_attendance """
    lp = lecture_path.split("_")[0]
    d = get_date_from_string(lecture_path.split("_")[1])
    if check == "true":
        lecture_attend(lp, date=d)
    else:
        lecture_absent(lp, date=d)
    return redirect(f'/{PAGE}/attendance?date={lecture_path.split("_")[1]}')


@bp.route(f'/{PAGE}/attendance', methods=["GET", "POST"])
def get_attendance():
    """ get_absent_attendance """
    context = {}
    if request.method == 'POST':
        req = request.form.to_dict()
        replacement_lecture(req)
        return redirect(f'/{PAGE}/attendance')
    else:
        lectures_attendance()

        date = None
        if "date" in request.args:
            date = request.args.get("date")

        context["lectures"] = get_today_lectures(date)
        context["translated_year"] = get_translated_divisions()
        context["translated_semesters"] = get_translated_semesters()
        context["regulations"] = get_regulations()
        context["rooms"] = get_all_rooms()
        context["instructors"] = get_instructors_data()
        context["instructors_name"] = get_instructors_name()
        return render_template(f'{PAGE}/attendance.html', context=context)


@bp.route(f'/{PAGE}s', methods=["GET", "POST"])
def handle_mod():
    """ get all items or post to add new """
    context = {}
    if request.method == 'POST':
        return render_template(f'{PAGE}/{PAGE}.html')
    else:
        lectures_attendance()
        context["lectures"] = get_lectures()
        context["translated_year"] = get_translated_divisions()
        context["regulations"] = get_regulations()
        return render_template(f'{PAGE}/{PAGE}s.html', context=context)


@bp.route(f'/{PAGE}/new', methods=["POST", "GET"])
def new_lecture():
    """ add new """
    context = {}
    context["lectures"] = get_lectures()
    context["divisions"] = get_all_divisions_departments()
    context["languages"] = get_translated_languages()
    context["programs"] = get_translated_programs()
    context["rooms"] = get_all_rooms()
    context["buildings"] = get_buildings()
    context["regulations"] = get_regulations()
    context["weekDays"] = get_translated_weekdays()

    context["regulation_id"] = None
    context["semester"] = None
    context["year"] = None
    context["exec"] = "manual"

    if request.method == "POST":
        req = request.form.to_dict()
        context["regulation_id"] = req["regulation_id"]
        context["semester"] = req["semester"]
        context["year"] = req["year"]
        context["exec"] = req["exec"]
        return render_template(f'{PAGE}/new-{PAGE}.html', context=context)
    else:
        lectures_attendance()
        return render_template(f'{PAGE}/new-{PAGE}.html', context=context)


@bp.route(f'/{PAGE}/update', methods=["POST"])
def update():
    """ post to update """
    return redirect(f'/{PAGE}')


@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_one(id):
    """ delete item """
    return redirect(f'/{PAGE}')


# API

@bp.route(f'/{PAGE}/data', methods=["POST"])
def get_data():
    """ Get Data """
    req = request.form.to_dict()
    program = None
    if "program" in req:
        if req["program"] != "NoProgram":
            program = Program(req["program"])
    return get_api_lectures_data(req["department_id"], Semester(req["semester"]), Division(int(req["year"])), req["regulation_id"], program, "lecture")


@bp.route(f'/{PAGE}s/data', methods=["GET"])
def get_lectures_data():
    """ Get Lectures Data """
    return get_lectures()


@bp.route(f'/{PAGE}/<path>', methods=["GET", "POST"])
def handle_lecture_data_by_path(path):
    if request.method == "POST":
        pass
    else:
        return get_lecture_by_path(path)


@bp.route(f'/{PAGE}/add', methods=["POST"])
def add_lecture():
    """ add new """
    errors = []
    req = json.loads(list(request.form.to_dict().keys())[0])

    # If this group table already exist remove it
    overwrite_group_table(req[0])

    for r in req:
        if r["instructor"] == "" or r["course"] == "" or r["room"] == "" or r["startTime"] == "":
            errors.append({
                "msg": "برجاء ملئ جميع البيانات قبل الحفظ",
                "path": r["path"],
                "prepath": None
            })
        error, path, prepath = add_new_lecture(r)
        if error:
            errors.append({
                "msg": error,
                "path": path,
                "prepath": prepath
            })

    if len(errors) > 0:
        return {
            "status": False,
            "errors": errors
        }
    else:
        return {
            "status": True,
            "msg": "تم الحفظ"
        }

# Need to check all primary keys with group num

# Need to check room with day with start time

# Need to check instructor with day with start time


