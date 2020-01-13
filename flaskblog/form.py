from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.model import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password =PasswordField('Password',validators=[DataRequired()])
    confirm_password =PasswordField('Confirm Passowrd',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('sign up')

    def validate_username(self,username):
        user =User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('that username is already taken! please try with other one')
    
    def validate_email(self,email):
        email =User.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError('that email is already taken! please try with other one')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password =PasswordField('Password',validators=[DataRequired()])
    # confirm_password =PasswordField('Confirm Passowrd',validators=[DataRequired()])
    remember =BooleanField('Remember Me')
    submit=SubmitField('sign up')