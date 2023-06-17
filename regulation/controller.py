from flask import flash
from regulation.model import Regulation
from database import db

def add_new_regulation(data):
    """
    Add a new regulation to the database.
    """
    regulation = Regulation(name=data['name'])
    db.session.add(regulation)
    db.session.commit()
    flash("تم اضافة الائحة", "success")

def delete_regulation(bid):
    """
    Delete a regulation from the database.
    """
    regulation = Regulation.query.get(bid)
    db.session.delete(regulation)
    db.session.commit()
    flash("تم حذف الائحة", "success")

def get_regulations():
    """
    Get all regulations from the database.
    """
    return Regulation.query.all()



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