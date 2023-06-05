from flask import Blueprint, redirect, render_template, request
from regulation.controller import add_new_regulation, delete_regulation

PAGE = 'regulation'

bp = Blueprint(PAGE, __name__, template_folder='templates')


@bp.route(f'/{PAGE}', methods=["POST"])
def add_regulation():
    """ add new """
    context = {}
    req = request.form.to_dict()
    add_new_regulation(req)
    return redirect('/settings')


@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_one(id):
    """ delete item """
    delete_regulation(id)
    return redirect(f'/settings')
