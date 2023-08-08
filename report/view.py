from flask import Blueprint, render_template, redirect, request
from course.controller import get_all_courses_general
from dashboard.controller import get_current_semester
from department.controller import get_departments
from instructor.controller import get_instructors_data, get_instructors_name
from lecture.controller import get_lectures
from regulation.controller import get_regulations
from utils.enums.Language import get_translated_languages

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
    context["lectures"] = get_lectures()
    return render_template(f'{PAGE}/attendance-report.html', context=context)


@bp.route(f'/form', methods=["GET"])
def get_form():
    """ get all items"""
    context = {}
    return render_template(f'{PAGE}/form.html')

@bp.route('/pdf')
def pdf():
    return render_template("pdf.html")