from flask import Blueprint, render_template, redirect, request
from course.controller import get_all_courses_general, get_course
from dashboard.controller import get_current_semester
from department.controller import get_departments
from instructor.controller import get_instructors_data, get_instructors_name
from lecture.controller import get_lecture_attendance_by_path, get_lecture_by_path, get_lectures
from regulation.controller import get_regulations
from utils.enums.Language import get_translated_languages
from utils.enums.Year import get_translated_divisions
from utils.enums.WeekDay import get_translated_weekdays
from utils.enums.Semester import get_translated_semesters

PAGE = 'report'

bp = Blueprint(PAGE, __name__, template_folder='templates')


@bp.route(f"/{PAGE}/summary_report", methods=['GET', 'POST'])
def show_Summary_report():
    """ Summary report on the lecturers """
    context = {}
    if request.method == 'POST':
        return redirect(f'/{PAGE}')
    else:
        return render_template(f'{PAGE}/Summary_report-{PAGE}.html')


@bp.route(f"/{PAGE}/detailed_report", methods=['GET', 'POST'])
def show_detailed_report():
    """ Detailed report on the lecturers """
    context = {}
    if request.method == 'POST':
        return redirect(f'/{PAGE}')
    else:
        return render_template(f'{PAGE}/detailed_report-{PAGE}.html')


@bp.route(f"/{PAGE}/weekly_report", methods=['GET', 'POST'])
def show_weekly_report():
    """ Weekly report on the lecturers """
    context = {}
    if request.method == 'POST':
        return redirect(f'/{PAGE}')
    else:
        return render_template(f'{PAGE}/weekly_report-{PAGE}.html')


@bp.route(f'/{PAGE}/attendance-report', methods=["GET"])
def attendance_report():
    """ attendance_report """
    context = {}
    context["current_semester"] = get_current_semester()
    context["days"] = get_translated_weekdays()
    context["years"] = get_translated_divisions()
    context["languages"] = get_translated_languages()
    context["semesters"] = get_translated_semesters()
    return render_template(f'{PAGE}/attendance-report.html', context=context)


@bp.route(f'/form', methods=["GET"])
def get_form():
    """ get all items"""
    context = {}
    return render_template(f'{PAGE}/form.html')

@bp.route('/pdf')
def pdf():
    return render_template("pdf.html")



@bp.route(f'/api/attendance-report/<id>/<path>', methods=["GET"])
def get_instructor_courses(id, path):
    return {
        "course": get_course(int(id)),
        "lecture": get_lecture_by_path(path),
        "lecture_attendance": get_lecture_attendance_by_path(path)
    }

