from flask import Blueprint, redirect, render_template, request


PAGE = 'instructor'

bp = Blueprint(PAGE, __name__, template_folder='templates')


@bp.route(f'/instructors', methods=["GET"])
def get_instructors():
    """ get all items or post to add new """
    context = {}
    return render_template(f'instructors.html')


@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_one(id):
    """ delete item """
    return redirect(f'/instructors')


@bp.route(f'/{PAGE}/new', methods=["GET", "POST"])
def new_one(id):
    """ new item """
    context = {}
    if request.method == 'POST':
        # return  changes
        return redirect('/instructors')
    else:
        return render_template(f'new-{PAGE}.html')


@bp.route(f'/{PAGE}/assign', methods=["GET", "POST"])
def new_assign():
    """ new item """
    context = {}
    if request.method == 'POST':
        # return  changes
        instructor_id = 0
        return redirect(f'/{PAGE}/{instructor_id}')
    else:
        return render_template(f'assign-{PAGE}.html')


@bp.route(f'/{PAGE}/<id>', methods=["GET", "POST"])
def get_instructor(id):
    """ get one item or post to update it """
    context = {}
    if request.method == 'POST':
        # return  changes
        return redirect(f'/{PAGE}/{id}')
    else:
        return render_template(f'{PAGE}.html')


