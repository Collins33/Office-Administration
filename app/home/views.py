from flask import render_template
from flask_login import login_required


from . import home#import the blueprint

@home.route('/')#route to render this view funtion
def homepage():
    return render_template('home/index.html',title="welcome")


@home.route('/dashboard')#this displays the dashboard
@login_required
def dashboard():
    #render dashboard template on /dashboard route
    return render_template('home/dashboard.html',title='dashboard')    