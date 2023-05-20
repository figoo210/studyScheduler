from flask import Blueprint, redirect, render_template, request


PAGE = 'instructor'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# THIS THE MAIN PAGE


@bp.route(f'/instructors', methods=["GET"])
def get_instructors():
    """ get all items or post to add new """
    context = {}
    return render_template(f'instructors.html', context=context)

# THIS FOR POP UP


@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_one(id):
    """ delete item """
    return redirect(f'/instructors')  # To the Route of instructor


# ADD INSTRUCTORE
@bp.route(f'/{PAGE}/new', methods=["GET", "POST"])
def new_one(id):
    """  new item """
    context = {}
    if request.method == 'POST':
        # return  changes
        return redirect('/instructors')
    else:
        return render_template(f'new-{PAGE}.html')

# Designation of materials


@bp.route(f'/{PAGE}/assign', methods=["GET", "POST"])
def dnew_assign():
    """ new item """
    context = {}
    if request.method == 'POST':
        # return  changes
        instructor_id = 0
        return redirect(f'/{PAGE}/{instructor_id}')
    else:
        return render_template(f'assign-{PAGE}.html')

# Profile personly


@bp.route(f'/{PAGE}/<id>', methods=["GET", "POST"])
def get_instructor(id):
    """ get all items or post to add new """
    context = {}
    if request.method == 'POST':
        return redirect(f'/{PAGE}/{id}')
    else:
        return render_template(f'{PAGE}.html')
