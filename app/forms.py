from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Enter Username ', validators=[DataRequired()])
    password = PasswordField('Enter Password ', validators=[DataRequired()])
    remember_me = BooleanField('Remember me?')
    submit = SubmitField('Sign In')
