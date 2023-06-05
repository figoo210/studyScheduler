from flask import Blueprint, redirect, render_template, request
from building.controller import add_new_building, delete_building

PAGE = 'building'

bp = Blueprint(PAGE, __name__, template_folder='templates')


@bp.route(f'/{PAGE}', methods=["POST"])
def add_building():
    """ add new """
    context = {}
    req = request.form.to_dict()
    add_new_building(req)
    return redirect('/settings')


@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_one(id):
    """ delete item """
    delete_building(id)
    return redirect(f'/settings')
