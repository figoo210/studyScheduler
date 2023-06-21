from flask import Blueprint, redirect, render_template, request
from instructor_role.controller import add_new_role, delete_role

PAGE = 'assign

bp = Blueprint(PAGE, __name__, template_folder='templates')


@bp.route(f'/{PAGE}', methods=["POST"])
def add_role():
    """ add new """
    context = {}
    req = request.form.to_dict()
    add_new_role(req)
    return redirect('/settings')


@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_one(id):
    """ delete item """
    delete_role(id)
    return redirect(f'/settings')
