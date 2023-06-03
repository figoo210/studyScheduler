from flask import Blueprint, redirect, render_template, request
from dashboard.controller import get_semesters_from_settings, get_semesters_dict, add_semester_settings
from department.controller import get_departments, get_arabic_divisions
from building.controller import get_buildings
from instructor_role.controller import get_roles
from regulation.controller import get_regulations
from utils.enums.Semester import Semester
from utils.date_and_time import get_string_from_date

PAGE = 'settings'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# setting page
@bp.route(f'/{PAGE}', methods=["GET"])
def show_settings():
    """ get one item or post to update it """
    context = {}
    # Get Semesters data
    semester_dates = get_semesters_from_settings()
    if semester_dates:
        context["semester_dates"] = {
            "semester": semester_dates.semester,
            "semester_start_date": get_string_from_date(semester_dates.semester_start_date),
            "semester_end_date": get_string_from_date(semester_dates.semester_end_date)
        }
    else:
        context["semester_dates"] = {
            "semester": None,
            "semester_start_date": None,
            "semester_end_date": None
        }
    context["semesters"] = get_semesters_dict()

    # Get departments data
    context["departments"] = get_departments()
    context["arabic_divisions"] = get_arabic_divisions()

    # Get buildings data
    context["buildings"] = get_buildings()

    # Get roles data
    context["roles"] = get_roles()

    # Get regulations data
    context["regulations"] = get_regulations()

    return render_template(f'{PAGE}.html', context=context)


# Add Dates
@bp.route(f'/{PAGE}/dates', methods=["POST"])
def add_dates():
    """ post to add term dates """
    req = request.form.to_dict()
    add_semester_settings(req)
    return redirect(f'/{PAGE}')

