from crypt import methods
from sre_constants import SUCCESS
from flask import Flask, render_template, flash ,get_flashed_messages, redirect, session, g, request
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, User, apiKey
from flask_debugtoolbar import DebugToolbarExtension
from forms import UserForm, LogInForm, DropDownForm
import requests as API_request
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///funfinder_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "gotasecret333"



connect_db(app)


@app.route('/', methods=['GET'])
def home_page():
    """displays home page"""
    
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
            flash("Welcome Back!")
        return redirect('/user')
    
    else:
        form.username.errors = ["incorrect name/ password"]    
    flash("You must be logged in to do that")
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def add_user(): 
    """Register user - display form and handle form submission"""
    form = UserForm()
    
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
    
# User routes 
@app.route('/user', methods=['GET'])
def list_users():
    """displays list of all users in db"""
    users = User.query.all()
    return render_template("allusers.html", users=users)


@app.route('/<int:uid>', methods=['GET',"POST"])
def show_user(uid):
    """show details about user based on user id"""
    form = DropDownForm()
    user = User.query.get_or_404(uid)
    session['user_id'] = user.id
    return render_template('userdetail.html', user=user, form=form, user_id=uid)

@app.route('/user/<int:uid>/edit', methods=['GET', 'POST'])
def edit_user(uid):
    u = User.query.get_or_404(uid)
    form = UserForm(obj=u)
    
    if form.validate_on_submit():
        u.name = form.name.data
        u.email = form.email.data
        u.state = form.state.data
        u.username = form.username.data
        u.password = form.password.data
        db.session.commit()
        flash("User Profile Updated")
        return redirect('/user') 
    return render_template("edituser.html", form=form)

@app.route('/user/<int:uid>/delete', methods=['GET','POST'])
def delete_user(uid):
    """delete user profile"""
    
    u = User.query.get_or_404(uid)
    
    db.session.delete(u)
    db.session.commit()
    flash ('User Deleted', 'success')
    
    return redirect('/register')
    
@app.route('/activity', methods=['POST'])
def activity():
    activity_id = request.form["activity"]
    return redirect(f"/park/{activity_id}")
    

# @app.route('/park', methods =['GET'])
# def display_parks():
#     """display park data based on search term"""
#     url = f"https://developer.nps.gov/api/v1/activities/parks?id=24380E3F-AD9D-4E38-BF13-C8EEB21893E7&api_key={apiKey}"

#     payload={}
#     headers = {}

#     response = API_request.request("GET", url, headers=headers, data=payload)

#     json_data = json.loads(response.text)
#     activity = json_data["data"][0]["name"]
#     parks = json_data["data"][0]["parks"]
#     # print(parks)
#     return render_template ('park.html', activity=activity,parks=parks)

@app.route('/park/<string:activity_id>', methods=['GET'])
def display_parks(activity_id):
    """display park data based on selected search term """
    url = f"https://developer.nps.gov/api/v1/activities/parks?id={activity_id}&api_key={apiKey}"
    
    payload={}
    headers = {}

    response = API_request.request("GET", url, headers=headers, data=payload)

    json_data = json.loads(response.text)
    activity = json_data["data"][0]["name"]
    parks = json_data["data"][0]["parks"]
    # print(parks)
    return render_template ('park.html', activity=activity,parks=parks)
    
    
@app.route('/logout')
def logout(): 
    """log User out and redirects to homepage. """
    
    session.pop("user_id")
    flash("You have logged out")
    return redirect('/')

    
    