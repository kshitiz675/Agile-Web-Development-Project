from flask import render_template, url_for, redirect
from app import app, models
#from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('Home.html', title='Home')

@app.route('/assessment/<int:quizId>')
def assessment(quizId):
    quiz = models.Quiz.query.filter_by(id=quizId).first()
    if quiz == None:
        #TODO not found page
        return "Not Found"
    return render_template('Assessment.html', title=quiz.quizname, quiz=quiz)

@app.route('/login', methods=['GET', 'POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
       return redirect('/index')
   return render_template('Login.html', title='Login', form=form)

@app.route('/registration')
def registration():
    return render_template('Registration.html', title='Registration')
