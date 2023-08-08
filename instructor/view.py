import json

from flask import Blueprint, redirect, render_template, request
from course.controller import get_all_courses_general
from instructor.controller import delete_instructor, get_instructors_data, add_new_instructor, get_instructors_name, get_instructor_data, instructor_search
from instructor_role.controller import get_roles
from instructor_course.controller import add_new_instructor_course, delete_instructor_course_by_id
from instructor_time.controller import add_new_time, delete_time
from department.controller import get_departments
from lecture.controller import get_instructor_lectures_statistics, get_instructor_lectures_table, lectures_attendance
from regulation.controller import get_regulations
from dashboard.controller import get_current_semester

from utils.enums.WeekDay import get_translated_weekdays

PAGE = 'instructor'

bp = Blueprint(PAGE, __name__, template_folder='templates')

# THIS THE MAIN PAGE
@bp.route(f'/instructors', methods=["GET"])
def get_instructors():
    """ get all items or post to add new """
    context = {}
    context["instructors"] = get_instructors_data()
    context["roles"] = get_roles()
    return render_template(f'{PAGE}/instructors.html', context=context)

# THIS FOR POP UP
@bp.route(f'/{PAGE}/delete/<id>', methods=["GET"])
def delete_one(id):
    """ delete item """
    delete_instructor(id)
    return redirect(f'/instructors')  # To the Route of instructor


# Remove instructor course
@bp.route(f'/{PAGE}/course/delete/<id>/<iid>', methods=["GET"])
def delete_ic(id, iid):
    """ delete instructor course """
    delete_instructor_course_by_id(id)
    return redirect(f'/instructor/{iid}')  # To the Route of instructor


# Remove instructor time
@bp.route(f'/{PAGE}/time/delete/<id>/<iid>', methods=["GET"])
def delete_it(id, iid):
    """ delete instructor it """
    delete_time(id)
    return redirect(f'/instructor/{iid}')  # To the Route of instructor


# ADD INSTRUCTORE
@bp.route(f'/{PAGE}/new', methods=["GET", "POST"])
def new_one():
    """  new item """
    context = {}
    if request.method == 'POST':
        req = json.loads(request.form.to_dict()["data"])
        for e in req:
            add_new_instructor(e)
        return redirect('/instructors')
    else:
        # get all roles
        context["roles"] = get_roles()
        # get all departments
        context["departments"] = get_departments()

        return render_template(f'{PAGE}/new-{PAGE}.html', context=context)


@bp.route(f'/{PAGE}/assign', methods=["GET", "POST"])
def new_assign():
    """ new item """
    context = {}
    if request.method == 'POST':
        req = json.loads(request.data)
        if len(req["instructor_course"]) >= 1:
            for ic in req["instructor_course"]:
                add_new_instructor_course(ic["instructor_id"], ic["course_id"], ic["groups_num"])
        if len(req["instructor_time"]) >= 1:
            for it in req["instructor_time"]:
                add_new_time(it["day_of_week"], it["start_time"], it["end_time"], it["instructor_id"])
        return redirect(f'/{PAGE}s')
    else:
        context["instructors"] = get_instructors_data()
        context["instructors_name"] = get_instructors_name()
        context["regulations"] = get_regulations()
        context["semester"] = get_current_semester()
        return render_template(f'{PAGE}/assign-{PAGE}.html', context=context)


# Profile personly
@bp.route(f'/{PAGE}/<id>', methods=["GET", "POST"])
def get_instructor(id):
    """ get all items or post to add new """
    context = {}
    if request.method == 'POST':
        return redirect(f'/{PAGE}/{id}')
    else:
        lectures_attendance()
        context["instructor"] = get_instructor_data(id)
        context["instructors"] = get_instructors_data()
        context["instructors_name"] = get_instructors_name()
        context["regulations"] = get_regulations()
        context["courses"] = get_all_courses_general()
        context["semester"] = get_current_semester()
        context["week_days"] = get_translated_weekdays()
        context["instructor_lectures_table"] = get_instructor_lectures_table(id)
        context["statistics"] = get_instructor_lectures_statistics(id)
        return render_template(f'{PAGE}/{PAGE}-profile.html', context=context)


# Instructors API

@bp.route(f'/api/instructors', methods=["GET"])
def get_all_instructors():
    return get_instructors_data()


@bp.route(f'/api/instructor/courses/<id>', methods=["GET"])
def get_instructor_courses(id):
    return get_instructor_lectures_table(id)


@bp.route('/api/instructors/search', methods=["POST"])
def search_courses():
    search_text = request.form['search_text']
    table_type = request.form['table_type']
    results = instructor_search(table_type, search_text)
    return results

