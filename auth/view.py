from flask import Blueprint, render_template, redirect, request
from flask_login import login_user
from auth.controller import login_validate, update_users, verify_validate, create_user, get_users, delete_user_by_id
PAGE = 'auth'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# login page
@bp.route(f'/login', methods=["GET", "POST"])
def login_page():
    """ sign in  """
    context = {}
    if request.method == 'POST':
        req = request.form.to_dict()
        is_valid, user = login_validate(req)
        if is_valid:
            login_user(user=user, remember=True)
            return redirect("/")
        return redirect("/login")
    else:
        return render_template(f'layout/login.html')

# forget password
@bp.route(f'/verification', methods=["POST"])
def verification():
    """ sign in  """
    context = {}
    req = request.form.to_dict()
    is_valid, user = verify_validate(req)
    if is_valid:
        login_user(user=user, remember=True)
        return redirect("/")
    return redirect("/logn")

# create user
@bp.route(f'/new-user', methods=["POST"])
def create_new_user():
    """ create new user  """
    req = request.form.to_dict()
    create_user(req["username"], req["password"])
    return redirect("/users")

# Show & update
@bp.route('/users', methods=["GET", "POST"])
def show_users():
    context = {}
    if request.method == 'POST':
        req = request.form.to_dict()
        print("#######################: ", req)
        update_users(req)
        return redirect("/users")
    else:
        # get all users data
        context["users"] = get_users()
        return render_template(f'users.html', context=context)

@bp.route('/user/delete/<id>')
def delete_user(id):
    """ delete user """
    delete_user_by_id(id)
    return redirect("/users")

