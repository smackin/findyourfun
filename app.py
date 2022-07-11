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
    

@app.route('/user', methods=['GET'])
def list_users():
    """displays list of all users in db"""
    users = User.query.all()
    return render_template("allusers.html", users=users)


@app.route('/<int:user_id>')
def show_user(user_id):
    """show details about user based on user id"""
    user = User.query.get_or_404(user_id)
    return render_template('userdetail.html', user=user)
    


@app.route('/find', methods=['GET'])
def find_function():
    """display form to search terms """
    
    return render_template('find.html')

@app.route('/park', methods =['GET'])
def display_parks():
    """display park data based on search term"""
    
    return render_template ('park.html')


    


@app.route('/logout')
def logout(): 
    """log User out and redirects to homepage. """
    
    session.pop("user_id")
    
    return redirect('/')

    
    