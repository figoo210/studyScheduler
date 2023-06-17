from flask import Blueprint, redirect, render_template, request
import json
from course.controller import get_all_courses_general, get_all_courses, get_course, create_course, delete_course_by_id
from dashboard.controller import get_semesters_dict, get_semesters_list
from regulation.controller import get_regulations
from department.controller import get_departments
from utils.enums.Year import Division



PAGE = 'course'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# Show courses
@bp.route('/courses', methods=["GET"])
def get_courses():
    """ get all courses  """
    context = {}
    context["semesters"] = get_semesters_list()
    context["dsemesters"] = get_semesters_dict()
    context["courses"] = get_all_courses_general()
    context["regulations"] = get_regulations()
    context["departments"] = get_departments()
    return render_template(f'{PAGE}/courses.html', context=context)

# popup
@bp.route(f'/{PAGE}/update', methods=["POST"])
def update_course_by_id():
    """ post to update """
    return redirect(f'/{PAGE}')

# Delete Course
@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_course(id):
    """ delete course """
    delete_course_by_id(id)
    return redirect(f'/courses')

# Add courses
@bp.route(f'/{PAGE}/new', methods=["GET", "POST"])
def new_coures():
    """ new course """
    context = {}
    if request.method == 'POST':
        req = json.loads(request.form.to_dict()["data"])
        print("#################: ", req)
        for e in req:
            has_section = False
            if "has_section" in e and e["has_section"] == "on":
                has_section = True
            create_course(
                e["name"],
                e["code"],
                e["credit_hrs"],
                e["semester"],
                int(e["year"]),
                e["language"],
                e["program"],
                has_section,
                e["regulation_id"],
                e["department_id"]
            )
        return redirect('/courses')
    else:
        context["semesters"] = get_semesters_list()
        context["dsemesters"] = get_semesters_dict()
        context["courses"] = get_all_courses_general()
        context["regulations"] = get_regulations()
        context["departments"] = get_departments()
        return render_template(f'{PAGE}/new-{PAGE}.html', context=context)



# Courses API
@bp.route('/api/courses', methods=["GET"])
def get_courses_name():
    return get_all_courses_general()
