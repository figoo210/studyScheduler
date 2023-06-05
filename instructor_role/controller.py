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



