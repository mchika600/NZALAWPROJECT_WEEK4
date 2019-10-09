from flask_sqlalchemy import SQLAlchemy 
from app_base import app,db 
from werkzeug.security import generate_password_hash, check_password_hash

# User Auth Flow Mixin
from flask_login import UserMixin

# Import login_manager
from app_base import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# One-to-many Relationship
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)  
    username = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), unique= True, nullable = False)
    password = db.Column(db.String(256), nullable = False)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def __repr__(self):
        return '{} has been created'.format(self.username)

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(150),unique= True, nullable = False)
    phone = db.Column(db.String(150),nullable = False)
    message = db.Column(db.String(500),nullable = False)

    def __init__(self,name,email,phone,message):
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message
    
    
    def __repr__(self):
        return "The Title is {} and the user is {}".format(self.title,self.name)