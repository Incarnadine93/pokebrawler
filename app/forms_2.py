from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class pokemonform(FlaskForm):
    pokemonname = StringField('Pokemon', validators = [DataRequired()])
    submit = SubmitField()