from flask import Blueprint, redirect, render_template, request

from course.controller import get_all_courses_general, get_all_courses, get_course
from dashboard.controller import get_semesters_dict, get_semesters_list


PAGE = 'course'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# Show courses
@bp.route('/courses', methods=["GET"])
def get_courses():
    """ get all courses  """
    context = {}
    context["semesters"] = get_semesters_list()
    context["courses"] = get_all_courses_general()
    return render_template(f'{PAGE}/courses.html', context=context)

# popup
@bp.route(f'/{PAGE}/update', methods=["POST"])
def update():
    """ post to update """
    return redirect(f'/{PAGE}')

# Delete Course
@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_course(id):
    """ delete course """
    return redirect(f'/courses')

# Add courses
@bp.route(f'/{PAGE}/new', methods=["GET", "POST"])
def new_coures(id):
    """ new course """
    context = {}
    if request.method == 'POST':
        # return  changes
        return redirect('/courses')
    else:
        return render_template(f'{PAGE}/new-{PAGE}.html', context=context)



# Courses API
@bp.route('/api/courses', methods=["GET"])
def get_courses_name():
    return get_all_courses_general()
