import json

from flask import Blueprint, redirect, render_template, request
from building.controller import get_buildings
from room.controller import get_all_rooms, create_room, delete_room, update_room

PAGE = 'room'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# THIS THE MAIN PAGE (ROOM)
@bp.route(f'/rooms', methods=["GET"])
def get_rooms():
    """ get all rooms or post to add new """
    context = {}
    context["buildings"] = get_buildings()
    context["rooms"] = get_all_rooms()
    return render_template(f'{PAGE}/rooms.html', context=context)


# update room
@bp.route(f'/{PAGE}/update', methods=["POST"])
def update_room_by_id():
    """ post to update """
    req = request.form.to_dict()
    update_room(
        room_id=req["id"],
        name=req["name"],
        building_id=req["building_id"],
        real_capacity=req["real_capacity"],
        supported_capacity=req["supported_capacity"]
    )
    return redirect(f'/{PAGE}s')


# Remove room
@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_room_by_id(id):
    """ delete item """
    delete_room(id)
    return redirect('/rooms')


# Add rooms
@bp.route(f'/{PAGE}/new', methods=["GET", "POST"])
def new_room():
    """ new room """
    context = {}
    if request.method == 'POST':
        req = json.loads(request.form.to_dict()["data"])
        for e in req:
            create_room(name=e["name"], building_id=e["building_id"], real_capacity=e["real_capacity"], supported_capacity=e["supported_capacity"])
        return redirect('/rooms')
    else:
        context["buildings"] = get_buildings()
        return render_template(f'{PAGE}/new-{PAGE}.html', context=context)
