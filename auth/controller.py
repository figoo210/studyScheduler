from flask import request, flash
from werkzeug.security import generate_password_hash
from database import db
from auth.model import User

# Forms Validate
def login_validate(req):
    user = User.query.filter_by(username=req["username"]).first()
    if not user:
        flash('خطاء في اسم المستخدم')
        return False, None
    if not user.verify_password(req["password"]):
        flash('خطاء في كلمة المرور')
        return False, None
    return True, user

def verify_validate(req):
    user = User.query.filter_by(username=req["username"]).first()
    if not user:
        flash('خطاء في اسم المستخدم')
        return False, None
    if user.pid != req["pid"]:
        flash('الرقم القومي غير صحيح')
        return False, None
    return True, user

def create_user(username, password):
    new_user = User(username=username, password=generate_password_hash(password, method="scrypt"), is_admin=False)
    db.session.add(new_user)
    db.session.commit()

