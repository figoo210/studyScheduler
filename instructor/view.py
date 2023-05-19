from flask import Blueprint, redirect, render_template, request


PAGE = 'instructor'

<<<<<<< HEAD
bp = Blueprint(PAGE, __name__, template_folder='templates')


@bp.route(f'/{PAGE}/<id>', methods=["GET", "POST"])
=======
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
>>>>>>> acdd6a4 (create auth and add to view)
def handle_one(id):
    """ get one item or post to update it """
    context = {}
    if request.method == 'POST':
<<<<<<< HEAD
        # return  changes
=======
>>>>>>> acdd6a4 (create auth and add to view)
        return render_template(f'{PAGE}.html')
    else:
        return render_template(f'{PAGE}.html')

# Designation of materials


<<<<<<< HEAD
@bp.route(f'/{PAGE}', methods=["GET", "POST"])
=======
@inst.route(f'/{PAGE}', methods=["GET", "POST"])
>>>>>>> acdd6a4 (create auth and add to view)
def handle_mod():
    """ get all items or post to add new """
    context = {}
    if request.method == 'POST':
        return render_template(f'{PAGE}.html')
    else:
<<<<<<< HEAD
        return render_template(f'doctors.html')


@bp.route(f'/{PAGE}/new', methods=["GET"])
def new_one(id):
    """ new item """
    return render_template(f'instructorname.html')


@bp.route(f'/{PAGE}/update', methods=["POST"])
=======
        return render_template(f'{PAGE}.html')


@inst.route(f'/{PAGE}/update', methods=["POST"])
>>>>>>> acdd6a4 (create auth and add to view)
def update():
    """ post to update """
    return redirect(f'/{PAGE}')


<<<<<<< HEAD
@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
=======
@inst.route(f'/{PAGE}/delete/<id>', methods=["GET"])
>>>>>>> acdd6a4 (create auth and add to view)
def delete_one(id):
    """ delete item """
    return redirect(f'/{PAGE}')
