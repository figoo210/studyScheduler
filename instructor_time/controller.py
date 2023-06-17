from flask import flash
from database import db
from instructor_role.model import InstructorTime 

def add_new_time(data):
    """
    Add a new time to the database.
    """
    time = InstructorTime(name=data['name'])
    db.session.add(time)
    db.session.commit()
    flash("تم اضافة التوقيت ", "success")

def delete_time(bid):
    """
    Delete a Time from the database.
    """
    time = InstructorTime.query.get(bid)
    db.session.delete(time)
    db.session.commit()
    flash("تم حذف التوقيت", "success")

def update_time(id,start_time,day_of_week,end_time):
    instructortime = InstructorTime.query.get(id)   
    instructortime.start_time = start_time
    instructortime.day_of_week = day_of_week
    instructortime.end_time = end_time
    db.session.commit()
    
def get_times():
    """
    Get all Times from the database.
    """
    return InstructorTime.query.all()

def is_form_empty(AuthForm):
    # Loop through all form fields
    for field in AuthForm.values():
        # Check if the field has a value
        if field.strip() != '':
            flash("لم يتم الحفظ")
            return False  # Form is not empty
        flash("تم الحفظ")
    return True  # Form is empty