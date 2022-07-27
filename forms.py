
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, SelectField, TextAreaField
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


class UserForm(FlaskForm):
    """Form for adding Users"""
    name = StringField("Your Name", validators=[InputRequired()])
    username = StringField("Your Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    email = StringField("Your Email", validators=[InputRequired()])
    state = SelectField('State', choices=[(st, st) for st in states])

    

class DropDownForm(FlaskForm):
    # location = SearchField("Where do you want to go? ")
    activity = SelectField("Select an Activity", choices=[
        ('09DF0950-D319-4557-A57E-04CD2F63FF42','Arts and Culture'),
('13A57703-BB1A-41A2-94B8-53B692EB7238','Astronomy'),
('5F723BAD-7359-48FC-98FA-631592256E35','Auto and ATV'),
('7CE6E935-F839-4FEC-A63E-052B1DEF39D2','Biking'),
('071BA73C-1D3C-46D4-A53C-00D5602F7F0E','Boating'),
('A59947B7-3376-49B4-AD02-C0423E08C5F7','Camping'),
('07CBCA6A-46B8-413F-8B6C-ABEDEBF9853E','Canyoneering'),
('BA316D0F-92AE-4E00-8C80-DBD605DC58C3','Caving'),
('B12FAAB9-713F-4B38-83E4-A273F5A43C77','Climbing'),
('C11D3746-5063-4BD0-B245-7178D1AD866C','Compass and GPS'),
('8C495067-8E94-4D78-BBD4-3379DACF6550','Dog Sledding'),
('AE42B46C-E4B7-4889-A122-08FE180371AE','Fishing'),
('D72206E4-6CD1-4441-A355-F8F1827466B1','Flying'),
('1DFACD97-1B9C-4F5A-80F2-05593604799E','Food'),
('3F3ABD16-2C52-4EAA-A1F6-4235DE5686F0','Golfing'),
('B33DC9B6-0B7D-4322-BAD7-A13A34C584A3','Guided Tours'),
('42FD78B9-2B90-4AA9-BC43-F10E9FEA8B5A','Hands-On'),
('BFF8C027-7C8F-480B-A5F8-CD8CE490BFBA','Hiking'),
('0307955A-B65C-4CE4-A780-EB36BAAADF0B','Horse Trekking'),
('8386EEAF-985F-4DE8-9037-CCF91975AC94','Hunting and Gathering'),
('5FF5B286-E9C3-430E-B612-3380D8138600','Ice Skating'),
('DF4A35E0-7983-4A3E-BC47-F37B872B0F25','Junior Ranger Program'),
('B204DE60-5A24-43DD-8902-C81625A09A74','Living History'),
('C8F98B28-3C10-41AE-AA99-092B3B398C43','Museum Exhibits'),
('4D224BCA-C127-408B-AC75-A51563C42411','Paddling'),
('0C0D142F-06B5-4BE1-8B44-491B90F93DEB','ParkFilm'),
('7779241F-A70B-49BC-86F0-829AE332C708','Playground'),
('42CF4021-8524-428E-866A-D33097A4A764','SCUBA Diving'),
('24380E3F-AD9D-4E38-BF13-C8EEB21893E7','Shopping'),
('F9B1D433-6B86-4804-AED7-B50A519A3B7C','Skiing'),
('3EBF7EAC-68FC-4754-B6A4-0C38A1583D45','Snorkeling'),
('C38B3C62-1BBF-4EA1-A1A2-35DE21B74C17','Snow Play'),
('7C912B83-1B1B-4807-9B66-97C12211E48E','Snowmobiling'),
('01D717BC-18BB-4FE4-95BA-6B13AD702038','Snowshoeing'),
('AE3C95F5-E05B-4A28-81DD-1C5FD4BE88E2','Surfing'),
('587BB2D3-EC35-41B2-B3F7-A39E2B088AEE','Swimming'),
('94369BFD-F186-477E-8713-AE2A745154DA','Team Sports'),
('4D06CEED-90C6-4B69-B264-32CC90B69BA6','Tubing'),
('8A1C7B17-C2C6-4F7C-9539-EA1E19971D80','Water Skiing'),
('0B685688-3405-4E2A-ABBA-E3069492EC50','Wildlife Watching'),
            ])
    
# class AddFavoriteForm():
    
    

