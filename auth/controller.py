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
    user = User.query.filter_by(username=username).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash("هذا المستخدم موجود بالفعل", "danger")
        return False

    new_user = User(username=username, password=generate_password_hash(password, method="scrypt"), is_admin=False)
    db.session.add(new_user)
    db.session.commit()
    flash("تم حفظ المستخدم", "success")
    return True

def get_users():
    users = User.query.all()
    return users

def update_users(data):
    admin_users = []
    for key in data:
        user_id, field = key.split("-")
        if field == "is_admin":
            admin_users.append(int(user_id))
        if not data[key] or data[key] == "" or field == "is_admin":
            continue
        elif field == "password":
            user = User.query.get(user_id)
            setattr(user, field, generate_password_hash(data[key], method="scrypt"))
            db.session.commit()

    for user in get_users():
        if user.id in admin_users:
            user.is_admin = True
        else:
            user.is_admin = False
        db.session.commit()

def delete_user_by_id(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

