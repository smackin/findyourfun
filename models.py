"""Models for findyourfun app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class 


"""connect db function to psql"""
def connect_db(app):
    db.app = app
    db.init_app(app)
