from flask import flash
from building.model import Building

from database import db

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
    return Building.query.all()



