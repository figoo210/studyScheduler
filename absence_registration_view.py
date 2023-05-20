from flask import Blueprint,  render_template, redirect, request


PAGE = 'absence_registration_view'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# Show absence


@bp.route(f'/{PAGE}/assign', methods=["GET", "POST"])
def show_absence():
    """ show or add or delete absence """
    context = {}
    if request.method == 'POST':
        # return  changes
        instructor_id = 0
        return redirect(f'/{PAGE}/{instructor_id}')
    else:
        return render_template(f'assign-{PAGE}.html')

# update lecture


@bp.route(f'/{PAGE}/update', methods=["POST"])
def update():
    """ post to update """
    return redirect(f'/{PAGE}')
