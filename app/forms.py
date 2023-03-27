from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class pSearch(FlaskForm):
    pokemonName = StringField('pokemonName', validators = [DataRequired()])
    submit = SubmitField()