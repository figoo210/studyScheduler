from flask import request , flash 
from database import db
from auth.model import Auth

# This func for route with using "wtform"


def welcome_to_dash(form):
    username = form.name.data
    password = form.league_division.data
    auth = Auth(username=username, password=password)
    db.session.add(auth)
    db.session.commit()

def is_form_empty(AuthForm):
    # Loop through all form fields
    for field in AuthForm.values():
        # Check if the field has a value
        if field.strip() != '':
            flash("لم يتم الحفظ")
            return False  # Form is not empty
        flash("تم الحفظ")
    return True  # Form is empty

"""
# To use this function
check = is_form_empty(AuthForm)
# True if form is empty, False otherwise
print(check)

"""
