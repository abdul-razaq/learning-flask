from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField

# create a new signup form inheriting from the base Form class
class SignupForm(Form):
	# create each field we want in the form
	first_name = StringField('First name')
	last_name = StringField('Last name')
	email = StringField('Email')
	password = PasswordField('Password')
	submit = SubmitField('Sign Up')
