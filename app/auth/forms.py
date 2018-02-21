from flask_wtf import FlaskForm

from wtforms import PasswordField,StringField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Email,EqualTo

from ..models import Employee

#create the RegistrationForm class
#it inherits the FlaskForm

class RegistrationForm(FlaskForm):
    #this is the form for users to create new accounts
    #the form fields below
    email=StringField('Email', validators=[DataRequired(),Email()])#each form contains validators to check the input
    username=StringField('Username',validators=[DataRequired()])
    first_name=StringField('First Name',validators=[DataRequired()])
    last_name=StringField('Last Name',validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password')])#ensure email is equal to confirm password field
    confirm_password=PasswordField('Confirm Password')

    #submit field will rep a button that users will be able to click to register
    submit=SubmitField('Register')


    #methods to validate email and username
    #they query data from the database
    #they ensure that email and username are not in the database

    def validate_email(self,field):
        #THIS VALIDATES THE EMAIL
        if Employee.query.filter_by(email=field.data).first():
            #RAISE VALUE ERROR IF EMAIL ALREADY EXISTS
            raise ValidationError('EMAIL ALREADY IN USE')


    def validate_username(self,field):
        #THIS CHECKS IF THE USERNAME EXISTS IN THE DATABASE
        if Employee.query.filter_by(username=field.data).first():
            #RAISE VALIDATION ERROR IF IT EXISTS
            raise ValidationError("Username already exists")


class LoginForm(FlaskForm):
    #form for users to log-in
    email=StringField('Email', validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Login')                    

