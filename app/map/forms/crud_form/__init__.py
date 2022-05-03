from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *


class location_form(FlaskForm):
    title = StringField("Title", [
        validators.DataRequired()
    ], description="Name of location")

    longitude = StringField("Longitude", [
        validators.DataRequired()
    ], description="Longitude coordinate value")

    latitude = StringField("Latitude", [
        validators.DataRequired()
    ], description="Latitude coordinate value")

    population = StringField("Population", description="Population count")
    submit = SubmitField()