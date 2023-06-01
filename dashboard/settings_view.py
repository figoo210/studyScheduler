from flask import Blueprint, redirect, render_template, request


PAGE = 'setting_view'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# setting page
@bp.route(f'/{PAGE}', methods=["GET", "POST"])
def show_sitting():
    """ get one item or post to update it """
    context = {}
    if request.method == 'POST':
        return render_template(f'{PAGE}.html')
    else:
        return render_template(f'{PAGE}.html')


# Add section (popup)
@bp.route(f'/{PAGE}/update', methods=["POST"])
def update():
    """ post to update """
    return redirect(f'/{PAGE}')


# Add user  (popup)
@bp.route(f'/{PAGE}/new', methods=["GET", "POST"])
def new_one(id):
    """ new user """
    context = {}
    if request.method == 'POST':
        # return  changes
        return redirect(f'/{PAGE}')
    else:
        return render_template(f'new-{PAGE}.html')


# user_page
@bp.route(f'/{PAGE}/<id>', methods=["GET", "POST"])
def get_user(id):
    """ get one user or post to update it """
    context = {}
    if request.method == 'POST':
        # return  changes
        return redirect(f'/{PAGE}/{id}')
    else:
        return render_template(f'{PAGE}.html')


# Delete user
@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_one(id):
    """ delete item """
    return redirect(f'/settings')


# Security information update
@bp.route(f'/{PAGE}/<id>', methods=["GET", "POST"])
def get_user(id):
    """ get one user or post to update it """
    context = {}
    if request.method == 'POST':
        # return  changes
        return redirect(f'/{PAGE}/{id}')
    else:
        return render_template(f'{PAGE}.html')
