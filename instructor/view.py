import json

from flask import Blueprint, redirect, render_template, request
from instructor.controller import delete_instructor, get_instructors_data, add_new_instructor, get_instructors_name, get_instructor_data
from instructor_role.controller import get_roles
from instructor_course.controller import add_new_instructor_course
from instructor_time.controller import add_new_time
from department.controller import get_departments
from regulation.controller import get_regulations
from dashboard.controller import get_current_semester

PAGE = 'instructor'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# THIS THE MAIN PAGE


@bp.route(f'/instructors', methods=["GET"])
def get_instructors():
    """ get all items or post to add new """
    context = {}
    context["instructors"] = get_instructors_data()
    return render_template(f'{PAGE}/instructors.html', context=context)

# THIS FOR POP UP


@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_one(id):
    """ delete item """
    delete_instructor(id)
    return redirect(f'/instructors')  # To the Route of instructor


# ADD INSTRUCTORE
@bp.route(f'/{PAGE}/new', methods=["GET", "POST"])
def new_one():
    """  new item """
    context = {}
    if request.method == 'POST':
        req = json.loads(request.form.to_dict()["data"])
        for e in req:
            add_new_instructor(e)
        return redirect('/instructors')
    else:
        # get all roles
        context["roles"] = get_roles()
        # get all departments
        context["departments"] = get_departments()

        return render_template(f'{PAGE}/new-{PAGE}.html', context=context)

# Designation of materials


@bp.route(f'/{PAGE}/assign', methods=["GET", "POST"])
def new_assign():
    """ new item """
    context = {}
    if request.method == 'POST':
        req = json.loads(request.data)
        for ic in req["instructor_course"]:
            add_new_instructor_course(
                ic["instructor_id"], ic["course_id"], ic["groups_num"])
        for it in req["instructor_time"]:
            add_new_time(it["day_of_week"], it["start_time"],
                         it["end_time"], it["instructor_id"])
        return redirect(f'/{PAGE}s')
    else:
        context["instructors"] = get_instructors_data()
        context["instructors_name"] = get_instructors_name()
        context["regulations"] = get_regulations()
        context["semester"] = get_current_semester()
        return render_template(f'{PAGE}/assign-{PAGE}.html', context=context)

# Profile personly


@bp.route(f'/{PAGE}/<id>', methods=["GET", "POST"])
def get_instructor(id):
    """ get all items or post to add new """
    context = {}
    if request.method == 'POST':
        return redirect(f'/{PAGE}/{id}')
    else:
        context["instructor"] = get_instructor_data(id)
        return render_template(f'{PAGE}/{PAGE}-profile.html', context=context)


# Instructors API

@bp.route(f'/api/instructors', methods=["GET"])
def get_all_instructors():
    return get_instructors_data()
