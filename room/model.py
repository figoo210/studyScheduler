from database import db


class Room(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    qr_code = db.Column(db.Text, unique=True, nullable=True)
    real_capacity = db.Column(db.Integer, unique=False, nullable=True)
    supported_capacity = db.Column(db.Integer, unique=False, nullable=True)
    section = db.relationship('Section', backref='room_sections', lazy=True)
    # backref create dumy column
    # section "this name of class Section "
    # laze import section attributes with room True mean dont include
    lectures = db.relationship('Lecture', backref='room_lectures', lazy=True)
    building_id = db.Column(db.Integer, db.ForeignKey("building.id"))
