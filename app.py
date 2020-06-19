from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# app = Flask(__name__)

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SECRET_KEY'] = 'P8s3_&/^H2pqBKf-3'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# bootstrap = Bootstrap(app)

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(256), unique=True)
#     image = db.Column(db.String(256), unique=True)
#     url = db.Column(db.String(256), unique=True)

#     def __repr__(self):
#         return '<Role %r>' % self.name

# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
#     password = PasswordField('Pasword', validators=[DataRequired()])
#     remember_me = BooleanField('Keep me logged in')
#     submit = SubmitField('Log In')

# class ArticleForm(FlaskForm):
#     title = StringField('Título', validators=[DataRequired()])
#     image = StringField('Url', validators=[DataRequired()])
#     url = StringField('Url Image', validators=[DataRequired()])
#     submit = SubmitField('Agregar')

# conda create -n flask python=3.6
# pip install flask
# pip install Flask-Bootstrap4
# pip install flask-wtf
# pip install flask-sqlalchemy
# pip install flask-mail
# pip install flask-migrate
# pip install flask-login
# pip install email_validator


# set FLASK_APP = app.py
# set FLASK_DEBUG=1
# set MAIL_USERNAME=<Gmail username>
# set MAIL_PASSWORD=<Gmail password>
# flask run

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/claroshop')
# def claroshop():
#     return render_template('claroshop.html')

# @app.route('/add_claroshop', methods=['GET', 'POST'])
# def add_claroshop():
#     form = ArticleForm()
#     if form.validate_on_submit():
#         flash("Regristro agregado correctamente")
#         return redirect(url_for('claroshop'))
#     return render_template('claro_form.html', form=form)

# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)

# Custom page errors
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500