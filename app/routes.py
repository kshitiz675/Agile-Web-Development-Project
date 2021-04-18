from flask import render_template, url_for, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('Theme and Purpose.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('Login.html', title='Login', form=form)

@app.route('/registration')
def registration():
    return render_template('Registration.html', title='Registration')
