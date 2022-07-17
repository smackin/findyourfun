from unicodedata import name
from flask_wtf import FlaskForm
from sqlalchemy import values
from wtforms import StringField, FloatField, EmailField, PasswordField, SelectField, SearchField
from wtforms.validators import InputRequired

states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
        'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
        'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
        'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
        'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

activities = [ 
            ("A59947B7-3376-49B4-AD02-C0423E08C5F7", "Camping"), 
            ("7779241F-A70B-49BC-86F0-829AE332C708","Playground"), 
            ("0B685688-3405-4E2A-ABBA-E3069492EC50","Wildlife Watching"),
            ("24380E3F-AD9D-4E38-BF13-C8EEB21893E7","Shopping"), 
            ("BFF8C027-7C8F-480B-A5F8-CD8CE490BFBA","Hiking"), 
            ("1DFACD97-1B9C-4F5A-80F2-05593604799E","Food"), 
            ("AE42B46C-E4B7-4889-A122-08FE180371AE","Fishing")]

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
    # location = SearchField("Where do you want to go? ")
    activity = SelectField("Select and Activity", choices=[
            ("A59947B7-3376-49B4-AD02-C0423E08C5F7", "Camping"), 
            ("7779241F-A70B-49BC-86F0-829AE332C708","Playground"), 
            ("0B685688-3405-4E2A-ABBA-E3069492EC50","Wildlife Watching"),
            ("24380E3F-AD9D-4E38-BF13-C8EEB21893E7","Shopping"), 
            ("BFF8C027-7C8F-480B-A5F8-CD8CE490BFBA","Hiking"), 
            ("1DFACD97-1B9C-4F5A-80F2-05593604799E","Food"), 
            ("AE42B46C-E4B7-4889-A122-08FE180371AE","Fishing")])
    

