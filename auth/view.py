from flask import Blueprint, render_template
from auth.forms import AuthForm
from auth.controller import welcome_to_dash

PAGE = 'auth'

aut = Blueprint(PAGE, __name__, template_folder='templates')


@aut.route(f'/{PAGE}', methods=['POST'])
def submit():
    form = AuthForm()
    if form.validate_on_submit():
        # change username and password
        welcome_to_dash(form)
        return render_template(f'{PAGE}.html')  # 'Welcome to the dashboard'
    else:
        # 'Invalid username or password'
        return render_template(f'{PAGE}.html')
