from database import db
from sqlalchemy.orm import backref


class InstructorCourse(db.Model):
    """
    argument of relationship must be capital like class name
    backref can be small because of the model
    laze prefare to be T
    in relations
    one :make db.relation and add column name s like courses
    many: make or put Foreign key on it and name single
    Foreign_key=can be small like ("instructor_time.id")
    """
    id = db.Column(db.Integer, primary_key=True)

    groups_num = db.Column(db.Integer, unique=False, default=1)
    instructor_id = db.Column(db.Integer, db.ForeignKey("instructor.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)

    lectures = db.relationship("Lecture", backref=backref("lecture"), lazy=True)

