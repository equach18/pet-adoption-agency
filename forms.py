from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, URLField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class AddPetForm(FlaskForm):
    """Form for adding pets"""
    name = StringField("Pet Name", validators=[InputRequired(message="Enter name.")])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine','Porcupine')], validators=[InputRequired()])
    photo_url = URLField("Photo URL", validators=[Optional(), URL(message="Enter valid URL.")])
    age = FloatField("Age", validators=[Optional(), NumberRange(0,30, message="Age must be 0-30")])
    notes = StringField("Notes", validators=[Optional()])
    
class EditPetForm(FlaskForm):
    """Form to edit a pet""" 
    photo_url = URLField("Photo URL", validators=[Optional(), URL(message="Enter valid URL.")])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Availability")