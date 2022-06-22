from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///funfinder_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "gotasecret333"

connect_db(app)


@app.route('/')
def home_page():
    """displayes home page"""
    return render_template('base.html')
