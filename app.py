import os

from flask import Flask, session, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager
# Import SQLAlchemy
# from sqlalchemy_utils import create_database, database_exists
from config import Config
from database import db

# Define the WSGI application object


def create_app(config_class=Config):
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(config_class)
    # app.app_context().push()

    # Check for database existing
    # if not database_exists(app.config.get("SQLALCHEMY_DATABASE_URI")):
    #     create_database(app.config.get("SQLALCHEMY_DATABASE_URI"))

    # Initialize Flask extensions here
    db.init_app(app)

    # Config
    # CORS(app)
    # CORS(app, resources={ r"/*": {"origins": "*"}}, supports_credentials=True)

    with app.app_context():
        from auth.model import User
        from building.model import Building
        from department.model import Department, DivisionDepartments
        from regulation.model import Regulation
        from room.model import Room
        from instructor.model import Instructor
        from course.model import Course, CourseUpdates
        from instructor_role.model import InstructorRole
        from instructor_time.model import InstructorTime
        from lecture.model import Lecture
        from dashboard.model import SemesterSettings
        from instructor_course.model import InstructorCourse
        db.create_all()
        db.session.commit()
        # Migrate(app, db, compare_type=True)
        User.create_admin_if_not_exist()
        Department.create_general_department_if_not_exist()
        DivisionDepartments.create_general_division_if_not_exist()

    # Import a module / component using its blueprint handler variable
    from dashboard.error_view import bp as error_view
    from dashboard.main_view import bp as main_view
    from dashboard.settings_view import bp as settings_view
    from department.view import bp as department_view
    from auth.view import bp as auth_view
    from course.view import bp as course_view
    from instructor.view import bp as instructor_view
    from building.view import bp as building_view
    from instructor_role.view import bp as role_view
    from regulation.view import bp as regulation_view
    from room.view import bp as room_view
    from lecture.view import bp as lecture_view

    # Register blueprint(s)
    app.register_blueprint(error_view)
    app.register_blueprint(main_view)
    app.register_blueprint(settings_view)
    app.register_blueprint(auth_view)
    app.register_blueprint(course_view)
    app.register_blueprint(instructor_view)
    app.register_blueprint(department_view)
    app.register_blueprint(building_view)
    app.register_blueprint(role_view)
    app.register_blueprint(regulation_view)
    app.register_blueprint(room_view)
    app.register_blueprint(lecture_view)

    # Sample HTTP error handling
    @app.errorhandler(404)
    def not_found(error):
        return redirect('/not-found')

    @app.route('/favicon.ico')
    def favicon():
        return "work"

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    # Login Manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login_page"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
