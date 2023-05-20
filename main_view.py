from flask import Blueprint,  render_template


PAGE = 'main_view'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# Show dash


@bp.route('/main_view', methods=["GET"])
def show_dash():
    """ get all item  """
    context = {}
    return render_template('main_view.html', context=context)
