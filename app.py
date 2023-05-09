import os

from flask import Flask, session
from flask_cors import CORS
from flask_migrate import Migrate
# Import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists
from config import Config
from database import db

# Define the WSGI application object
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.app_context().push()

    # Check for database existing
    if not database_exists(app.config.get("SQLALCHEMY_DATABASE_URI")):
        create_database(app.config.get("SQLALCHEMY_DATABASE_URI"))

    # Initialize Flask extensions here
    db.init_app(app)

    # Config
    CORS(app)
    cors = CORS(app, resources={ r"/*": {"origins": "*"}}, supports_credentials=True)
    migrate = Migrate(app, db, compare_type=True)

    # Import a module / component using its blueprint handler variable
    from course.view import bp as course_view
    from course.model import Course

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

    db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
