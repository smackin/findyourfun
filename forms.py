from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, EmailField, PasswordField, SelectField, SearchField
from wtforms.validators import InputRequired

states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
        'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
        'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
        'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
        'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

activities = [ "Camping", "Playground", "Wildlife" ,"Shopping", "Hiking", "Food", "Fishing"]

class LogInForm(FlaskForm):
    """form to log in user"""
    username = StringField("username", validators=[InputRequired()])
    password = PasswordField("password")


class RegisterForm(FlaskForm):
    """Form for adding Users"""
    name = StringField("Your Name", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    username = StringField("Your Username", validators=[InputRequired()])
    email = EmailField("Your Email", validators=[InputRequired()])
    state = SelectField('State', choices=[(st, st) for st in states])
    

class SearchForm(FlaskForm):
    location = SearchField("Where do you want to go? ")
    activity = SelectField("What do you want to do", choices=[(act, act) for act in activities])
    

