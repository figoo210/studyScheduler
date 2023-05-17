from database import db


class Auth(db.Model):

    """
    argument of relationship must be capital like class name
    backref can be small because of the model
    laze prefare to be T
    in relations
    one :make db.relation and add column name s like courses
    many: make or put Foreign key on it and name single _id
    db.ForeignKey("")can be small like ("instructor_time.id")

    """
    # can we add id or use the username(admin) as a Primary_key
    # This page doesnt conncet to any moduels
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    username = db.Column(db.String(65), unique=False, nullable=False)
    password = db.Column(db.Integer, unique=True, nullable=False)
