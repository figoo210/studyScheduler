from flask import Blueprint, redirect, render_template, request
from lecture.controller import get_lectures
from regulation.controller import get_regulations
from department.controller import get_all_divisions_departments
from room.controller import get_all_rooms
from building.controller import get_buildings

from utils.enums.Program import get_translated_programs
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


@bp.route(f'/{PAGE}s', methods=["GET", "POST"])
def handle_mod():
    """ get all items or post to add new """
    context = {}
    if request.method == 'POST':
        return render_template(f'{PAGE}/{PAGE}.html')
    else:
        context["lectures"] = get_lectures()
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


@bp.route(f'/{PAGE}/add', methods=["POST"])
def add_lecture():
    """ add new """
    context = {}
    req = request.form.to_dict()
    print("#############################: ", req)
    return "200"


@bp.route(f'/{PAGE}/update', methods=["POST"])
def update():
    """ post to update """
    return redirect(f'/{PAGE}')


@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_one(id):
    """ delete item """
    return redirect(f'/{PAGE}')
