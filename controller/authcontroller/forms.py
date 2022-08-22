from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, BooleanField

class RegisterForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=12)])
    email = StringField('Email', [validators.DataRequired()])
    password = PasswordField('New password', [
        validators.DataRequired(),
        validators.EqualTo('password_confirm', message='Password must be matched')
    ])
    password_confirm = PasswordField('Repeat password')
    