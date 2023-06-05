from flask import Blueprint, render_template
from dashboard.controller import get_instructors_count, get_courses_count, get_rooms_count, get_lectures_count, get_instructors_sample

PAGE = 'main_view'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# Show dash


@bp.route('/', methods=["GET"])
def show_dash():
    """ get all item  """
    context = {}
    context["instructors_count"] = get_instructors_count()
    context["courses_count"] = get_courses_count()
    context["rooms_count"] = get_rooms_count()
    context["lectures_count"] = get_lectures_count()

    context["instructors_sample"] = get_instructors_sample(10)

    return render_template('main.html', context=context)
