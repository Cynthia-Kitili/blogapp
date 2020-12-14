from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo,ValidationError
from ..models import User


class UpdateProfile(FlaskForm):
    bio = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('Post')

class PitchForm(FlaskForm):
    content = TextAreaField('Your pitch')
    submit = SubmitField('post')

class CommentForm(FlaskForm):
    comment_id = TextAreaField('WRITE COMMENT')
    submit = SubmitField('SUBMIT')    