from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class EnterNumber(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired()])