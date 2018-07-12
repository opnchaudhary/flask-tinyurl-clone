# coding:utf-8
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, URL

class URLShortenerForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Shorten')
