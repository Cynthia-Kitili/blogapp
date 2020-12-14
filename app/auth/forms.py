from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Enter Email Address:',validators=[DataRequired(),Email()])
    username = StringField('Enter  username:',validators = [DataRequired()])
    password = PasswordField('Enter Password:',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('Username already taken.Kindly enter a different one.')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Email already taken.Kindly enter a different one.')

class LoginForm(FlaskForm):
    email = StringField('Enter Email:',validators=[DataRequired()])
    password = PasswordField('Enter Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')