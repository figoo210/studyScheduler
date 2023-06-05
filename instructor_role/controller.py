from flask import flash
from instructor_role.model import InstructorRole
from database import db

def add_new_role(data):
    """
    Add a new role to the database.
    """
    role = InstructorRole(name=data['name'])
    db.session.add(role)
    db.session.commit()
    flash("تم اضافة الرتبة", "success")

def delete_role(bid):
    """
    Delete a role from the database.
    """
    role = InstructorRole.query.get(bid)
    db.session.delete(role)
    db.session.commit()
    flash("تم حذف الرتبة", "success")

def get_roles():
    """
    Get all roles from the database.
    """
    return InstructorRole.query.all()



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