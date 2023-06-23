from database import db
from sqlalchemy.orm import backref


class InstructorRole(db.Model):
    """
    argument of relationship must be capital like class name
    backref can be small because of the model
    laze prefare to be T
    in relations
    one :make db.relation and add column name s like courses
    many: make or put Foreign key on it and name single
    Foreign_key=can be small like ("instructor_time.id")
    """
    # role  الرتبة
    name = db.Column(db.String(30), primary_key=True)
    description = db.Column(db.Text, unique=False, nullable=True)

    instructors = db.relationship(
        "Instructor", backref=backref("role_instructors"), lazy=True)
