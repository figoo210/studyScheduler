from flask import Blueprint, render_template, redirect, request


PAGE = 'report'

bp = Blueprint(PAGE, __name__, template_folder='templates')


@bp.route(f"/{PAGE}/summary_report", methods=['GET', 'POST'])
def show_Summary_report():
    """ Summary report on the lecturers """
    context = {}
    if request.method == 'POST':
        return redirect(f'/{PAGE}')
    else:
        return render_template(f'Summary_report-{PAGE}.html')


@bp.route(f"/{PAGE}/detailed_report", methods=['GET', 'POST'])
def show_detailed_report():
    """ Detailed report on the lecturers """
    context = {}
    if request.method == 'POST':
        return redirect(f'/{PAGE}')
    else:
        return render_template(f'detailed_report-{PAGE}.html')


@bp.route(f"/{PAGE}/weekly_report", methods=['GET', 'POST'])
def show_weekly_report():
    """ Weekly report on the lecturers """
    context = {}
    if request.method == 'POST':
        return redirect(f'/{PAGE}')
    else:
        return render_template(f'weekly_report-{PAGE}.html')


@bp.route(f'/form', methods=["GET"])
def get_form():
    """ get all items"""
    context = {}
    return render_template(f'form.html')
