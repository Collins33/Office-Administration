from flask import flash,redirect,render_template,url_for
from flask_login import login_required,login_user,logout_user


#import auth blueprint
from . import auth
#import the forms class
from forms import RegistrationForm,LoginForm
#import the db
from .. import db
#import the models
from ..models import Employee


#the register view function
@auth.route('/register', methods=['GET', 'POST'])
def register():
    #handles request to /register method
    #gets the form input and crate Employee instance and save instance to the database

    #first create RegistrationForm instance
    form=RegistrationForm()
    
    #validate the form
    if form.validate_on_submit():
        #create employee object
        employee=Employee(
            email=form.email.data,
            username=form.username.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=form.password.data
        )

        #add employee into the database
        db.session.add(employee)
        db.session.commit()

        #flash message
        flash("You have successfully registered, You can now log in")

        #redirect to the login page
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form, title='Register')




@auth.route('/login', methods=['GET','POST'])
def login():
    #handle requests to login route
    # if employee queried exits,log in

    #create loginform object
    form=LoginForm()

    #check if form is validated
    if form.validate_on_submit():
        #if validate, query to get user who matches the email in the form
        employee=Employee.query.filter_by(email=form.email.data).first()

        #check if employee exists
        #check if the queried employee has password equal to what was on the form
        #verify_password compares the password in the form and the one in the database
        if employee is not None and employee.verify_password(form.password.data):
            #if the credentials meet the requirements, log them in
            #login_user is flask method to log-in user
            login_user(employee)

            #after logging them in,direct them to the dashboard view function
            return redirect(url_for('home.dashboard'))

        #if login details are false
        # send a flash message
        flash('Invalid email or password')


    #load the login template
    return render_template('auth/login.html', form=form, title='Login')        