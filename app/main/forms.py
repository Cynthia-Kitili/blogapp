from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo,ValidationError
from ..models import User


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    content = TextAreaField('Enter Your Blog:')
    submit = SubmitField('Submit')    

class CommentForm(FlaskForm):
    comment_id = TextAreaField('Leave A Comment:')
    submit = SubmitField('Submit')        