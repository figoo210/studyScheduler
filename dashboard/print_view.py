from flask import Blueprint, render_template, redirect, request
from instructor.controller import get_instructors_data, get_instructors_name

from lecture.controller import get_today_lectures
from building.controller import get_buildings
from room.controller import get_all_rooms
from utils.enums.WeekDay import get_translated_weekdays
from utils.enums.Year import get_translated_divisions

PAGE = 'print'

bp = Blueprint(PAGE, __name__, template_folder='templates')


@bp.route(f'/print/<paper>', methods=['GET'])
def printer(paper):
    """ Printer """
    context = {}
    if paper == "attendance-sheet":
        context["lectures"] = get_today_lectures()
        context["days"] = get_translated_weekdays()
        context["years"] = get_translated_divisions()
        context["buildings"] = get_buildings()
        context["hours"] = list(range(8, 21))
        context["rooms"] = get_all_rooms()
        return render_template('print/attendance-sheet.html', _target='print', context=context)
    else:
        return render_template(f'layout/404.html')


