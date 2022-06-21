"""Models for findyourfun app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

def connect_db(app):
    """connect db function to psql"""
    db.app = app
    db.init_app(app)
class User(db.Model): 
    """User"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False ,unique=True) 
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False ,unique=True)
    APIKey = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(2), nullable=False)


class Parks(db.Model):
    """Parks"""
    __tablename__ = "Parks"
    id = db.Column(db.Integer, primary_key =True)
    Name = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text)
    activities = db.Column(db.Text)
    
class Activities(db.Model): 
    """Activities sorted by Park"""
    __tablename__ = "Activities at each Park"
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)
    Parks.id = db.Column(db.Text)
    
class Favorites(db.Model):
    """users favorites"""
    id = db.Column(db.Integer, primary_key=True)
    User.id = db.Column(db.Integer, ForeignKey)
    Name = db.Column(db.Text, nullable = False)
    Parks.id = db.Column(db.Integer)


