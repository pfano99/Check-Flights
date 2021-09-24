from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, DateField
from wtforms.validators import DataRequired

class FlightForm(FlaskForm):
    departure = SelectField('From', choices=['OR Tambo International Airport', 
                                            'Cape Town International Airport', 
                                            'King Shaka International Airport',
                                            'Port Elizabeth Airport', 
                                            'East London Airport'] )
    arrival = SelectField('To', choices=['OR Tambo International Airport', 
                                            'Cape Town International Airport', 
                                            'King Shaka International Airport',
                                            'Port Elizabeth Airport', 
                                            'East London Airport'] )
    submit = SubmitField('Search')