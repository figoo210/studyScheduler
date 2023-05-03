import os
from datetime import timedelta
class Config:

    # Statement for enabling the development environment
    DEBUG = True


    # Define the database - we are working with
    SQLALCHEMY_DATABASE_URI = ""
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = os.urandom(24)

    # Sessions
    SESSION_PERMANENT = True
    SESSION_TYPE = "filesystem"
    PERMANENT_SESSION_LIFETIME = timedelta(hours = 24)

    # Secret key for signing cookies
    SECRET_KEY = os.urandom(24)
    JWT_SECRET_KEY = "svhbkeuivbhb94832vb94832vfHVHVuydg98732f984fg"