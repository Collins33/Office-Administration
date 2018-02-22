from flask import render_template,abort
from flask_login import login_required,current_user


from . import home#import the blueprint

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")


#this is the view function that renders the admin dashboard
# only admin users can access it
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    #check if current user is the admin
    if not current_user.is_admin:
        abort(403)


    return render_template('home/admin_dashboard.html', title="Dashboard")    
