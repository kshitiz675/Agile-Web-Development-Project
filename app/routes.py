from flask import render_template, url_for, redirect, flash
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from app.models import User, Quiz
#from flask_login import login_required
#Place @login_required for pages that require users to be signed in

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('Home.html', title='Home')

@app.route('/content')
def content():
    return render_template('Content.html', title='Content')

@app.route('/blockchain-test')
def blockchain():
    return render_template('Blockchain-test.html', title='Blockchain-test')

@app.route('/assessment')
def assessmentHome():
    return "Assessment Home Page"
   
@app.route('/assessment/<int:quizId>')
def assessment(quizId):
    # There must be a variable that defines which topic this quiz will cover
    quiz = Quiz.query.filter_by(id=quizId).first()
    if quiz == None: return 'Not Found'
    return render_template('Assesment.html', title='Assessment', quiz=quiz)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect('/index')
    return render_template('Login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/registration')
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('Registration.html', title='Registration', form=form)
