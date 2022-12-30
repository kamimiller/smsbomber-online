from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired

class EnterNumber(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired()])
    redeem = StringField('Redeem')
    
class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class Redeem(FlaskForm):
    redeem = StringField('Redeem', validators=[DataRequired()])
    date_end = DateField('Date', validators=[DataRequired()])