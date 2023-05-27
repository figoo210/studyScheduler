from flask import Blueprint, redirect, render_template, request


PAGE = 'report'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# THIS THE MAIN PAGE (ROOM)


@bp.route(f'/rooms', methods=["GET"])
def get_rooms():
    """ get all rooms or post to add new """
    context = {}
    return render_template(f'rooms.html')

# update room


@bp.route(f'/{PAGE}/update', methods=["POST"])
def update_room():
    """ post to update """
    return redirect(f'/{PAGE}')

# Remove room


@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_room(id):
    """ delete item """
    return redirect('/rooms')

# Add rooms


@bp.route(f'/{PAGE}/new', methods=["GET", "POST"])
def new_coures(id):
    """ new room """
    context = {}
    if request.method == 'POST':
        # return  changes
        return redirect('/rooms')
    else:
        return render_template(f'new-{PAGE}.html')
