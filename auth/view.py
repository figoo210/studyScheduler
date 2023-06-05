from flask import Blueprint, render_template, redirect, request
from flask_login import login_user
from auth.controller import login_validate, verify_validate
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
        return render_template(f'layout/login.html')
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

# Create new user
# @bp.route('/users', methods=["GET", "POST"])
# def signup_post():
#     # code to validate and add user to database goes here
#     email = request.form.get('email')
#     name = request.form.get('name')
#     password = request.form.get('password')

#     user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

#     if user: # if a user is found, we want to redirect back to signup page so user can try again
#         return redirect(url_for('auth.signup'))

#     # create a new user with the form data. Hash the password so the plaintext version isn't saved.
#     new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

#     # add the new user to the database
#     db.session.add(new_user)
#     db.session.commit()

#     return redirect(url_for('auth.login'))
