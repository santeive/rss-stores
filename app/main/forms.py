from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ArticleForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    image = StringField('Url', validators=[DataRequired()])
    url = StringField('Url Image', validators=[DataRequired()])
    submit = SubmitField('Agregar')

class ArticleFormUpdate(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    url = StringField('Url', validators=[DataRequired()])
    image = StringField('Url Image', validators=[DataRequired()])
    submit = SubmitField('Actualizar')

class ArticleFormDelete(FlaskForm):
    submit = SubmitField('Eliminar')
