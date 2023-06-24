import json
from flask import Blueprint, redirect, render_template, request
from lecture.controller import add_new_lecture, get_lectures, get_api_lectures_data
from regulation.controller import get_regulations
from department.controller import get_all_divisions_departments
from room.controller import get_all_rooms
from building.controller import get_buildings

from utils.enums.Program import get_translated_programs, Program
from utils.enums.Semester import Semester
from utils.enums.Year import Division, get_translated_divisions
from utils.enums.Language import get_translated_languages
from utils.enums.WeekDay import get_translated_weekdays


PAGE = 'lecture'

bp = Blueprint(PAGE, __name__, template_folder='templates')


@bp.route(f'/{PAGE}/<id>', methods=["GET", "POST"])
def handle_one(id):
    """ get one item or post to update it """
    context = {}
    if request.method == 'POST':
        return render_template(f'{PAGE}/{PAGE}.html')
    else:
        return render_template(f'{PAGE}/{PAGE}.html')



# @bp.route(f'/{PAGE}/absent/<id>', methods=["GET"])
# def set_absent_attendance(id):
#     """ set_absent_attendance """
#     record_attendance(id)
#     return redirect(f'{PAGE}/absent')



@bp.route(f'/{PAGE}/attendance', methods=["GET"])
def set_absent_attendance():
    """ get_absent_attendance """
    context = {}
    context["lectures"] = get_lectures()
    context["translated_year"] = get_translated_divisions()
    context["regulations"] = get_regulations()
    return render_template(f'{PAGE}/attendance.html', context=context)


@bp.route(f'/{PAGE}s', methods=["GET", "POST"])
def handle_mod():
    """ get all items or post to add new """
    context = {}
    if request.method == 'POST':
        return render_template(f'{PAGE}/{PAGE}.html')
    else:
        context["lectures"] = get_lectures()
        context["translated_year"] = get_translated_divisions()
        context["regulations"] = get_regulations()
        return render_template(f'{PAGE}/{PAGE}s.html', context=context)


@bp.route(f'/{PAGE}/new', methods=["POST", "GET"])
def new_lecture():
    """ add new """
    context = {}
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
    return get_api_lectures_data(req["department_id"], Semester(req["semester"]), Division(int(req["year"])), req["regulation_id"], Program(req["program"]))



@bp.route(f'/{PAGE}/add', methods=["POST"])
def add_lecture():
    """ add new """
    context = {}
    req = json.loads(list(request.form.to_dict().keys())[0])
    for r in req:
        if r["instructor"] == "" or r["course"] == "" or r["room"] == "" or r["startTime"] == "":
            return {
                "status": False,
                "msg": "برجاء ملئ جميع البيانات قبل الحفظ",
                "path": r["path"],
            }
        lectures = get_lectures()
        for lecture in lectures:
            lecture_range = int(lecture["course"]["credit_hrs"]) - 1 # before & after
            r1 = int(r["startTime"].split(":")[0]) - lecture_range
            r2 = int(r["startTime"].split(":")[0]) + lecture_range
            time_range = [item for item in range(r1, r2+1)]
            print("########################################: ", time_range)

            if lecture["instructor_id"] == r["instructor"] and \
                int(lecture["start_time"].split(":")[0]) in time_range and \
                lecture["day_of_week"] == r["day"]:
                return {
                    "status": False,
                    "msg": f"هذا المحاضر غير متاح في هذا الوقت لمادة {lecture['course'].name} لدكتور {lecture['instructor']['name']}",
                    "path": r["path"],
                }
            if lecture["room_id"] == r["room"] and \
                int(lecture["start_time"].split(":")[0]) in time_range and \
                lecture["day_of_week"] == r["day"]:
                return {
                    "status": False,
                    "msg": f"هذه المكان مشغول في هذا الوقت لمادة {lecture['course'].name} لدكتور {lecture['instructor']['name']}",
                    "path": r["path"],
                }
            new_lecture = add_new_lecture(r)

        if len(lectures) == 0:
            new_lecture = add_new_lecture(r)


    return {
        "status": True,
        "msg": "تم الحفظ"
    }

# Need to check all primary keys with group num

# Need to check room with day with start time

# Need to check instructor with day with start time
