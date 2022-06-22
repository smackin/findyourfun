"""Models for findyourfun app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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