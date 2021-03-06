from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required


#import admin blueprint
from . import admin
#import the forms class
from .forms import DepartmentForm, RoleForm
#import the db
from .. import db
#import the models
from ..models import Department,Role

def check_admin():
    #prevent users who are not admin from acessing the page
    if not current_user.is_admin:
        abort(403)



#DEPARTMENT VIEW FUNCTIONS
#show all departments
@admin.route('/departments', methods=['POST', 'GET'])
@login_required
def list_department():
    #it checks if you are an admin
    check_admin()
    #query db to get all the departments
    departments=Department.query.all()
    
    #render the departments template and pass the queried department to the template
    return render_template('admin/departments/departments.html', departments=departments, title="departments")




#add a department
@admin.route('/departments/add', methods=['GET','POST'])
@login_required
def add_department():
    #adds a department to the database
    #check if user is an admin
    check_admin()

    add_department=True

    #create Department form object
    form=DepartmentForm()

    #check if form is validated
    if form.validate_on_submit():
        #create department object
        department=Department(name=form.name.data, description=form.description.data)

        try:
            #add department to the database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a department')

        except:
            #throw exception if department already exists
            flash("Department already exists")

        #after adding the department, admin is redirected to view function with list of departments
        return redirect(url_for('admin.list_department'))
    
    #load the template with the form to add department
    return render_template('admin/departments/department.html', action="Add",add_department=add_department, form=form,title="Add Department")



@admin.route("/departments/edit/<int:id>", methods=['GET','POST'])
@login_required
def edit_department(id):
    #the route to edit a department
    #it takes the id as parameter which will be passed to it in the template

    #check if user is an admin
    check_admin()

    add_department=False
    
    #query the database for the department with the passed id
    department=Department.query.get_or_404(id)

    #create a form object
    form=DepartmentForm(obj=Department)

    #check if form is validate
    if form.validate_on_submit():
        #edit the department info with what is in the form
        department.name=form.name.data #name that is in the form
        department.description=form.name.description #description of in the form
        db.session.commit()

        flash("You have successfully edited the department")
    #replace the form data with info from the department
    form.name.data=department.name
    form.description.data=department.description

    return redirect(url_for("admin.list_department"))

    #render the template
    return render_template("/admin/departments/department.html", action="Edit", add_department=add_department,form=form,department=department,title="Edit department")




#the view function to delete a department
@admin.route("/departments/delete/<int:id>", methods=["GET","POST"])
@login_required
def delete_department(id):
    #check if you are an admin
    check_admin()

    #query db for the department
    department=Department.query.get_or_404(id)

    #delete the department from the db
    db.session.delete(department)
    db.session.commit()
    flash("You have successfully deleted the department")

    #redirect to the view function with the list of departments
    return redirect(url_for("admin.list_department"))

    return render_template(title="Delete Department")





#ROLE VIEW FUNCTION


@admin.route("/roles")
@login_required
def list_roles():

    #check if user is an admin
    check_admin()
    #list all roles

    #query db to get all roles
    roles=Role.query.all()

    #render the template
    return render_template("admin/roles/role.html",title="All roles",roles=roles)



@admin.route("/roles/add", methods=["POST","GET"])
@login_required
def add_role():
    #check if a user is an admin
    check_admin()

    add_role=True

    #create instance of roleform
    form=RoleForm()

    #check if form is valid
    if form.validate_on_submit():
        #create role object from form data
        role=Role(name=form.name.data, description=form.description.data)

        #add role to database if it does not exist
        try:
            db.session.add(role)
            db.session.commit()
            #confirmation if added well
            flash("You have added a role")
        except:
            #incase the role exists
            flash("The role already exists")

        #redirect to the page with all the roles
        return redirect(url_for("admin.list_roles"))


    #render the role template
    return render_template("admin/roles/role.html",add_role=add_role,form=form,title="Add role")


#view function to edit a role
@admin.route("/roles/edit/<int:id>" methods=["POST","GET"])
@login_required
def edit_roles(id):

    #check admin
    check_admin()

    add_role=False

    #get the specific role that matches the id
    role=Role.query.get_or_404(id)#throw 404 error if the role does not exist
    #create roleform object
    form=RoleForm(obj=role)

    #validate the form
    if form.validate_on_submit():
        #replace role name in db with the one in the form
        role.name=form.name.data
        #replace role desc in db with the one in the form
        role.description=form.description.data

        #add the new role to the db
        db.session.add(role)
        db.session.commit

        #confirmation message
        flash("You have successfully updated the role")

        #redirect to the role_list
        return redirect(url_for("admin.list_roles"))

    form.description.data=role.description
    form.name.data=role.name

    return render_template('admin/roles/role.html', add_role=add_role, form=form, title="Edit role")


#view function to delete a role
@admin.route("roles/delete/<int:id>" methods=["POST","GET"]) 
@login_required
def delete_role(id):
    #check if user an admin
    check_admin()

    #query the database for the role that matches the id
    role=Role.query.get_or_404(id)

    #delete the role from the db
    db.session.delete(role)
    db.session.commit()

    flash("You have successfully deleted the role")

    #redirect to the view function with all the roles
    return redirect(url_for("admin.list_roles"))

    return render_template(title="Delete role")

