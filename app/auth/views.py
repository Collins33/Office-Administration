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