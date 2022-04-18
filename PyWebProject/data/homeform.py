from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import wtforms
from wtforms.validators import DataRequired


class AddressDownloadForm(FlaskForm):
    address = StringField('Введите адрес ссылки', validators=[DataRequired()])
    submit_address = SubmitField('Найти')


class DownloadForm(FlaskForm):
    submit_download = SubmitField("Скачать")
