from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	firstname = StringField('First Name', validators=[DataRequired('Please enter your first name.')])
	lastname = StringField('Last Name', validators=[DataRequired('Please enter your last name.')])
	email = StringField('Email Address', validators=[DataRequired('Please enter your email address.'), Email('Please enter your email address.')])
	password = PasswordField('Password', validators=[DataRequired('Please enter a password.'), Length(min=6, message='Password must be 6 characters or more.')])
	submit = SubmitField('SIGNUP')

