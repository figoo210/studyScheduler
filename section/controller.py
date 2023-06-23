from flask import flash
from database import db
from section.model import Section 
from course.model import Course 

def add_new_section(data):
    """
    Add a new section to the database.
    """
    section = Section(course_id=data['course_id'],instructor_id=data['instructor_id'])
    db.session.add(section)
    db.session.commit()
    flash("تم اضافه سكشن ", "success")

def update_section(room_id,start_time,day_of_week,name,absent):
    section = Section.query.get()   
    section.room_id = room_id 
    section.start_time = start_time
    section.day_of_week = day_of_week
    section.name = name
    section.absent = absent
    db.session.commit()


def check_course_has_section(id):
    course = Course.query.get(id)
    section = Section.query.get(name=course.name)  
    if course.has_section == True:
        if section:
            return add_new_section()
    
def get_sections():
    """
    Get all lectures from the database.
    """
    return Section.query.all()

def delete_time(bid):
    """
    Delete a Time from the database.
    """
    section = Section.query.get(bid)
    db.session.delete(section)
    db.session.commit()
    flash("تم حذف السكشن ", "success")


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