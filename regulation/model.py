from database import db

class Regulation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)
    courses = db.relationship('Course', backref='course', lazy=True)
