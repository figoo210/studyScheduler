from flask import Blueprint, render_template, redirect, request

PAGE = 'error'

bp = Blueprint(PAGE, __name__, template_folder='templates')


@bp.route(f'/error', methods=['GET', 'POST'])
def show_error():
    """ show error to user Go back or Go to dashboard """
    if request.method == 'POST':
        return render_template(f'{PAGE}.html')
    else:
        return render_template(f'{PAGE}.html')


@bp.route(f'/not-found', methods=['GET'])
def show_error():
    """ show error to user Go back or Go to dashboard """
    return render_template(f'layout/404.html')


