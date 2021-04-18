from flask import render_template, url_for
from app import app
#from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('Theme and Purpose.html', title='Home')
"""
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('Login.html', title='Sign In', form=form)
"""
