from flask import Blueprint, redirect, render_template, request


PAGE = 'report'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# THIS THE MAIN PAGE (ROOM)


@bp.route(f'/rooms', methods=["GET"])
def get_rooms():
    """ get all rooms or post to add new """
    context = {}
    return render_template(f'rooms.html')

# add room


@bp.route(f'/{PAGE}/update', methods=["POST"])
def update_room():
    """ post to update """
    return redirect(f'/{PAGE}')

# Remove room


@bp.route(f'/{PAGE}/delete/<id>', methods=["POST"])
def delete_room(id):
    """ delete item """
    return redirect('/rooms')
