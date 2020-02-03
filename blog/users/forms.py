# Form related import
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
# User related import
from flask_login import current_user
from blog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),  Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),  Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message="Passwords MUST match!")])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
        
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')
        return

    def check_username(self, field):

        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been used already!')
        return

class UpdateUserForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')


    def check_email(self, field):
        
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')
        return

    def check_username(self, field):

        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been used already!')
        return
