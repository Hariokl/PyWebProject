from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DownloadForm(FlaskForm):
    address = StringField('Введите адрес ссылки', validators=[DataRequired()])
    submit = SubmitField('Войти')