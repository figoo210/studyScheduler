import json

from flask import Blueprint, redirect, render_template, request
from instructor.controller import delete_instructor, get_instructors_data, add_new_instructor, get_instructors_name
from instructor_role.controller import get_roles
from department.controller import get_departments
from regulation.controller import get_regulations


PAGE = 'instructor'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# THIS THE MAIN PAGE
@bp.route(f'/instructors', methods=["GET"])
def get_instructors():
    """ get all items or post to add new """
    context = {}
    context["instructors"] = get_instructors_data()
    return render_template(f'instructors.html', context=context)

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

        return render_template(f'new-{PAGE}.html', context=context)

# Designation of materials
@bp.route(f'/{PAGE}/assign', methods=["GET", "POST"])
def new_assign():
    """ new item """
    context = {}
    if request.method == 'POST':
        # return  changes
        instructor_id = 0
        return redirect(f'/{PAGE}/{instructor_id}')
    else:
        context["instructors"] = get_instructors_data()
        context["instructors_name"] = get_instructors_name()
        context["regulations"] = get_regulations()
        return render_template(f'assign-{PAGE}.html', context=context)

# Profile personly
@bp.route(f'/{PAGE}/<id>', methods=["GET", "POST"])
def get_instructor(id):
    """ get all items or post to add new """
    context = {}
    if request.method == 'POST':
        return redirect(f'/{PAGE}/{id}')
    else:
        return render_template(f'{PAGE}.html')


# Instructors API

@bp.route(f'/api/instructors', methods=["GET"])
def get_all_instructors():
    return get_instructors_data()

