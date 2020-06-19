from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Ingresar')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
    'Usernames must have only letters, numbers, dots or underscores')])
    password = PasswordField('Contraseña', validators=[DataRequired(), EqualTo('password2', message='Las contraseñas deben ser iguales.')])
    password2 = PasswordField('Confirmar contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrar')

    # Validamos que el email no exista
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Ya existe una cuenta registrada con este correo.')
    
    # Validamos que el usuario no exista
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Ya existe una cuenta registrada con este usuario')


