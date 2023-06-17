from database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):

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
    #one user(admin) have many permissions
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    username = db.Column(db.String(65), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean)
    pid = db.Column(db.String(14), unique=True, nullable=True)
    qa = db.Column(db.String(120), unique=False, nullable=True)

    def create_admin_if_not_exist():
        if not User.query.filter_by(username="admin").first():
            # if admin is not in the table
            # add admin
            admin = User(username="admin", password=generate_password_hash("admin", method="scrypt"), is_admin=True)
            db.session.add(admin)
            db.session.commit()

    def verify_password(self, password):
        return check_password_hash(self.password, password)

