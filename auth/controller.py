from flask import request
from database import db
from auth.model import Auth

# This func for route with using "wtform"


def welcome_to_dash(form):
    username = form.name.data
    password = form.league_division.data
    auth = Auth(username=username, password=password)
    db.session.add(auth)
    db.session.commit()
