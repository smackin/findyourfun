from crypt import methods
from flask import Flask, render_template, flash ,get_flashed_messages, redirect, session
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension
from forms import RegisterForm, LogInForm

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
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """user login form"""
    form = LogInForm()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        #authenticate will return a user or False. 
        user = User.authenticate(username, password)
        
        if user: 
            session['user_id'] = user.id #keep user logged in
        return redirect('/user')
    
    else:
        form.username.errors = ["incorrect name/ password"]    
    
    return render_template('login.html', form=form)

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
        return redirect('/user')
    else:
        return render_template('register.html', form=form)
    

@app.route('/user')
def userpage():
    """displays users homepage only if user in session"""
    
    if "user_id" not in session:
        flash("You must be logged in to access", "danger")    
        return redirect('/login')
    
    else:
        return render_template("user.html")

@app.route('/logout')
def logout(): 
    """log User out and redirects to homepage. """
    
    session.pop("user_id")
    
    return redirect('/')

    
# @app.route('user/login', methods=['GET', 'POST'])
# def login_user():
    