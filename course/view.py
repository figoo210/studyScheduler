from flask import Blueprint, redirect, render_template, request


PAGE = 'course'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# Show courses


@bp.route('/courses', methods=["GET"])
def get_courses():
    """ get all courses  """
    context = {}
    return render_template('courses.html')

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
        return render_template(f'new-{PAGE}.html')
