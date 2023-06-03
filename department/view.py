from flask import Blueprint, redirect, render_template, request
from department.controller import delete_department, add_new_department, update_department_count

PAGE = 'department'

bp = Blueprint(PAGE, __name__, template_folder='templates')


@bp.route(f'/{PAGE}', methods=["POST"])
def add_department():
    """ add new """
    context = {}
    req = request.form.to_dict()
    add_new_department(req)
    return redirect('/settings')


@bp.route(f'/{PAGE}/count', methods=["POST"])
def count_department():
    """ add new """
    context = {}
    req = request.form.to_dict()
    update_department_count(req)
    return redirect('/settings')


@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_one(id):
    """ delete item """
    delete_department(id)
    return redirect(f'/settings')


