from flask import Blueprint, redirect, render_template, request


PAGE = 'instructor'

inst = Blueprint(PAGE, __name__, template_folder='templates')

# THIS THE MAIN PAGE


@inst.route(f'/{PAGE}/<id>', methods=["GET"])
def instructorfunc(id):
    """ get one item or post to update it """
    return render_template(f'{PAGE}.html')

# THIS FOR POP UP


@inst.route(f'/{PAGE}/delete/<id>', methods=["POST"])
def delete_instrucor_name(id):
    """ delete item """
    return redirect(f'/{PAGE}')


# ADD INSTRUCTORE
@inst.route(f'/{PAGE}/<id>', methods=["GET", "POST"])
def add_instructors(id):
    """ get all items or post to add new """
    context = {}
    if request.method == 'POST':
        return render_template(f'{PAGE}.html')
    else:
        return render_template(f'{PAGE}.html')

# Designation of materials


@inst.route(f'/{PAGE}/<id>', methods=["GET", "POST"])
def designation_materials(id):
    """ get all items or post to add new """
    context = {}
    if request.method == 'POST':
        return render_template(f'{PAGE}.html')
    else:
        return render_template(f'{PAGE}.html')

# Profile personly


@inst.route(f'/{PAGE}/<id>', methods=["GET", "POST"])
def profile_personly(id):
    """ get all items or post to add new """
    context = {}
    if request.method == 'POST':
        return render_template(f'{PAGE}.html')
    else:
        return render_template(f'{PAGE}.html')
