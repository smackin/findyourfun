from crypt import methods
from flask import Flask, render_template, flash ,get_flashed_messages, redirect, session
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension
from forms import RegisterForm, UserLogInForm


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

@app.route('/users', methods=['GET', 'POST'])
def login_user():
    """user login form"""
    form = UserLogInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
    return redirect('')

@app.route('/register', methods=['GET', 'POST'])
def add_user(): 
    """Register user - display form and handle form submission"""
    form = RegisterForm()
    
    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        password = form.password.data
        email = form.email.data
        state = form.state.data
        
        user=  User.register(name, username, password, email, state)
        db.session.add(user)
        db.session.commit()
        
        session['user_id'] = user.id
        # flash (f'Created new User {username}, welcome {name}')
        return redirect('/')
    else:
        return render_template('register.html', form=form)
    

@app.route('/users')
def show_users():
    """displays users homepage"""
    
    return render_template('user_home.html')
    
    

    
# @app.route('user/login', methods=['GET', 'POST'])
# def login_user():
    