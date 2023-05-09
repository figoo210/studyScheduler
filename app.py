import os

from flask import Flask, session
from flask_cors import CORS
from flask_migrate import Migrate
# Import SQLAlchemy
# from sqlalchemy_utils import create_database, database_exists
from config import Config
from database import db

# Define the WSGI application object
def create_app(config_class=Config):
    app = Flask(__name__)
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
    # Migrate(app, db, compare_type=True)

    with app.app_context():
        from building.model import Building
        from department.model import Department
        from regulation.model import Regulation
        from room.model import Room
        from instructor.model import Instructor
        from course.model import Course
        from instructor_role.model import InstructorRole
        from instructor_time.model import InstructorTime
        from lecture.model import Lecture
        from section.model import Section
        db.create_all()
        db.session.commit()

    # Import a module / component using its blueprint handler variable
    from course.view import bp as course_view

    # Register blueprint(s)
    app.register_blueprint(course_view)

    # Sample HTTP error handling
    @app.errorhandler(404)
    def not_found(error):
        return 404

    @app.route('/favicon.ico')
    def favicon():
        return "work"

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'


    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
