from database import db
from sqlalchemy.orm import backref

class Regulation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)
    courses = db.relationship('Course', backref=backref('regulation_courses'), lazy=True)
