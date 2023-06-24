from flask import flash
from building.model import Building

from database import db, model_to_dict

def add_new_building(data):
    """
    Add a new building to the database.
    """
    building = Building(name=data['name'])
    db.session.add(building)
    db.session.commit()
    flash('تم اضافة المبنى', 'success')

def delete_building(bid):
    """
    Delete a building from the database.
    """
    building = Building.query.get(bid)
    db.session.delete(building)
    db.session.commit()
    flash('تم حذف المبنى','info')

def get_buildings():
    """
    Get all buildings from the database.
    """
    buildings = []
    for building in Building.query.all():
        buildings.append(model_to_dict(building))
    return buildings



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