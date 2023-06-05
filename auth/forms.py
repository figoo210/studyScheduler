from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
# we import data_required(func) or DataRequired(class)


class AuthForm(FlaskForm):
    username = StringField(label='UserName', validators=[DataRequired])
    password = PasswordField(label='Password', validators=[DataRequired])


