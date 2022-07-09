"""Models for findyourfun app."""

from flask_sqlalchemy import SQLAlchemy
import bcrypt
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model): 
    """Site User"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False ,unique=True) 
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False ,unique=True)
    state = db.Column(db.String(2), nullable=False)
    
    #register method
    @classmethod
    def register(cls, name, username, password, email, state):
        """register user with hashed pw & return user"""
    
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        
        #return instance of user with name, un, hashedpw, email, state
        return cls(name=name, username=username, password=hashed_utf8, email=email, state=state)
    #end_register_user


class Parks(db.Model):
    """Parks"""
    __tablename__ = "parks"
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text)
    activities = db.Column(db.Text)
    
class Activities(db.Model): 
    """Activities sorted by Park"""
    __tablename__ = "activities"
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)
    park_id = db.Column(db.Integer, db.ForeignKey('parks.id'))
    
class Favorites(db.Model):
    """users favorites"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    Name = db.Column(db.Text, nullable = False)
    park_id = db.Column(db.Integer, db.ForeignKey('parks.id'))


def connect_db(app):
    """connect db function to psql"""
    db.app = app
    db.init_app(app)