from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Enter Title:', validators=[DataRequired()])
    content = TextAreaField('Enter Blog:', validators=[DataRequired()])
    submit = SubmitField('Submit')