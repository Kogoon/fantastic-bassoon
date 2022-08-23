from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


# Register
class UserCreateForm(FlaskForm):
    name = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=20)])
    user_id = StringField('사용자 ID', validators=[DataRequired(), Length(min=4, max=10)])
    password = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password_confirm', '비밀번호가 일치하지 않습니다')])
    password_confirm = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])


# Login
class UserLoginForm(FlaskForm):
    user_id = StringField('사용자 아이디', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

