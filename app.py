from crypt import methods
from flask import Flask, render_template, flash ,get_flashed_messages, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddUserForm

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

@app.route('/users/new', methods=['GET', 'POST'])
def add_user(): 
    """Add user"""
    form = AddUserForm()
    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        password = form.password.data
        email = form.email.data
        state = form.state.data
        
        nwusr =  User(name=name, 
                    username=username,
                    password=password, 
                    email=email, 
                    state=state)
        db.session.add(nwusr)
        db.session.commit()
        # flash (f'Created new User {username}, welcome {name}')
        return redirect('/')
    else:
        return render_template('add_user_form.html', form=form)
    

    
# @app.route('user/login', methods=['GET', 'POST'])
# def login_user():
    