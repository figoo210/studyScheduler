from flask import Blueprint, redirect, render_template, request


PAGE = 'regulation'

regu = Blueprint(PAGE, __name__, template_folder='templates')


@regu.route(f'/{PAGE}/<id>', methods=["GET", "POST"])
def handle_one(id):
    """ get one item or post to update it """
    context = {}
    if request.method == 'POST':
        return render_template(f'{PAGE}.html')
    else:
        return render_template(f'{PAGE}.html')


@regu.route(f'/{PAGE}', methods=["GET", "POST"])
def handle_mod():
    """ get all items or post to add new """
    context = {}
    if request.method == 'POST':
        return render_template(f'{PAGE}.html')
    else:
        return render_template(f'{PAGE}.html')


@regu.route(f'/{PAGE}/update', methods=["POST"])
def update():
    """ post to update """
    return redirect(f'/{PAGE}')


@regu.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_one(id):
    """ delete item """
    return redirect(f'/{PAGE}')
