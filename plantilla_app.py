from flask import Flask
app = Flask(__name__)

# conda create -n flask python=3.6
# pip install flask

# set FLASK_APP = app.py
# set FLASK_DEBUG=1
# flask run

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)