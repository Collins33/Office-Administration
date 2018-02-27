from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

#create the department form as a class that inherits from FlaskForm
class DepartmentForm(FlaskForm):
    #for the admin to add or edit a department
    name=StringField('Name',validators=[DataRequired()])
    description=StringField('Description',validators=[DataRequired()])
    submit=SubmitField('submit')




#create the form to add the roles
class RoleForm(FlaskForm):
    name=StringField('name',validators=[DataRequired()])
    description=StringField('description',validators=[DataRequired()])
    submit=SubmitField('submit')    