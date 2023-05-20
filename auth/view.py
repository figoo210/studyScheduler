from flask import Blueprint, render_template, redirect, request
from auth.forms import AuthForm
from auth.controller import welcome_to_dash

PAGE = 'auth'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# login page


@bp.route(f'/login/<id>', methods=["GET", "POST"])
def login_page(id):
    """ sign in  """
    context = {}
    if request.method == 'POST':
        # return  changes(main_view.py)
        return render_template(f'{PAGE}.html')
    else:
        return render_template(f'{PAGE}.html')


# forget password
@bp.route(f'/verification/<id>', methods=["GET", "POST"])
def verification(id):
    """ sign in  """
    context = {}
    if request.method == 'POST':
        # return  changes
        return redirect(f'/{PAGE}/{id}')
    else:
        return render_template(f'{PAGE}.html')
