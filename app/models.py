from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class Employee(db.Model,UserMixin):
    #create the table name
    #should be in plural form of the model
    __tablename__='employees'

    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(60),index=True,unique=True)
    username=db.Column(db.String(60),index=True,unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    department_id=db.Column(db.Integer,db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)


    @property
    def password(self):
        #prevent password from being accessed
        #raise value error if you try to access password

        raise ValueError('password not a readable value')

    @password.setter
    def password(self,password):
        #set password to a hashed password
        self.password_hash=generate_password_hash(password)   

    def verify_password(self,password):
        #check if hashed password mathches actual password
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return '<Employee: {}>'.format(self.username)'  


#set up the user loader
# it will return the employee who mathches the user id stored in the session
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))       

