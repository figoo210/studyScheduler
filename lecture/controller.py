from flask import flash
from database import db
from lecture.model import Lecture

def add_new_lecture(data):
    """
    Add a new lecture to the database.
    """
    lecture = Lecture(course_id=data['course_id'],instructor_id=data['instructor_id'])
    db.session.add(lecture)
    db.session.commit()
    flash("تم اضافة الماده ", "success")
    
def update_lecture(room_id,start_time,day_of_week,name,absent):
    
    lecture = Lecture.query.get()   
    lecture.room_id = room_id 
    lecture.start_time = start_time
    lecture.day_of_week = day_of_week
    lecture.name = name
    lecture.absent = absent
    db.session.commit()

def get_lectures():
    """
    Get all lectures from the database.
    """
    return Lecture.query.all()

def delete_time(bid):
    """
    Delete a Time from the database.
    """
    lecture = Lecture.query.get(bid)
    db.session.delete(lecture)
    db.session.commit()
    flash("تم حذف الماده ", "success")


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
