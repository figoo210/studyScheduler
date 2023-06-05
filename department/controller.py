from flask import flash
from department.model import Department, DivisionDepartments
from database import db

arabic_divisions = ["الأولى", "الثانية", "الثالثة", "الرابعة"]

def get_departments():
    departments = []
    for dep in Department.query.all():
        department = {
            'id': dep.id,
            'name': dep.name,
            'divisions': get_department_divisions(dep.id)
        }
        departments.append(department)
    return departments

def get_division_name(division_num):
    return arabic_divisions[division_num - 1]

def get_arabic_divisions():
    di = {
        "1": "الأولى",
        "2": "الثانية",
        "3": "الثالثة",
        "4": "الرابعة"
    }
    return di

def get_department_divisions(department_id):
    divisions = []
    for dd in DivisionDepartments.query.filter_by(department_id=department_id).all():
        division = {
            "id": dd.id,
            "name": get_division_name(dd.division),
            "count": dd.students_count
        }
        divisions.append(division)
    return divisions

def delete_department(department_id):
    department = Department.query.get(department_id)
    if department:
        for dd in DivisionDepartments.query.filter_by(department_id=department_id).all():
            db.session.delete(dd)
        db.session.delete(department)
        db.session.commit()
        flash("تم حذف القسم", "info")
        return True
    return False


def add_new_department(data):
    department = Department(name=data['name'])
    db.session.add(department)
    db.session.commit()
    divisions = data['divisions'].split(",")
    for division in divisions:
        division_department = DivisionDepartments(department_id=department.id, division=int(division))
        db.session.add(division_department)
        db.session.commit()
    flash("تم اضافة القسم بنجاح", "success")


def update_department_count(data):
    for key in data:
        if not data[key] or data[key] == "":
            continue
        else:
            division_department = DivisionDepartments.query.get(int(key.split("-")[0]))
            division_department.students_count = data[key]
            db.session.commit()
            flash("تم تعديل القسم بنجاح", "success")

