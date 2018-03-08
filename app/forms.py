from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	aUsername = StringField("Username", validators=[DataRequired()])
	aPassword = PasswordField("Password", validators=[DataRequired()])
	aRemeber_Me = BooleanField("Remember Me?")
	aSubmit = SubmitField("Log in")
