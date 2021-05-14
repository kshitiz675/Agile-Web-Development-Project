from flask import render_template, url_for, redirect, flash, request, jsonify, session
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from app.models import TopicSection, User, Quiz, Topic, Question, Answer, UserResult, QuizResult
from flask_login import login_required
#Place @login_required for pages that require users to be signed in

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('Home.html', title='Home')

@app.errorhandler(404)
def error404(e):
    return render_template('404.html', title='error 404')

@app.errorhandler(500)
def error500(e):
    return render_template('500.html', title='error 500')

@app.route('/lesson')
@login_required
def content():
    return render_template('Content.html', title='Learn')

@app.route('/feedback/<int:id>')
@login_required
def feedback(id):
    feedback = Quiz.query.filter_by(id=id).first()
    if feedback == None: return 'Not Found'
    return render_template('Feedback.html', title='Feedback', feedback=feedback)

@app.route('/statistics')
def statistics():
    quizResults = QuizResult.getResultsForAllQuizzes()
    return render_template('Statistics.html', title='Statistics', results=quizResults, quizzes=Quiz.query.all())

@app.route('/lesson/<int:id>')
@login_required
def lesson(id):
    lesson = Topic.query.filter_by(id=id).first()
    if lesson == None: return 'Not Found'
    return render_template('Lesson.html', title='Lesson', lesson=lesson)

@app.route('/assessment/<int:quizId>', methods=['GET', 'POST'])
@login_required
def assessment(quizId):
    # There must be a variable that defines which topic this quiz will cover
    if request.method == 'GET':
        quiz = Quiz.query.filter_by(id=quizId).first()
        if quiz == None: return 'Not Found'
        return render_template('Assesment.html', title='Assessment', quiz=quiz)
    if request.method == 'POST':
        data = request.get_json()
        answers = data['answers']
        numQuestions = len(answers)
        numCorrect = 0
        for answer in answers:
            questionId = answer['questionId']
            answerId = answer['answerId']
            questionObj = Question.query.filter_by(id=questionId).first()
            if questionObj == None:
                return "Invalid"
            answerObj = Answer.query.filter_by(id=answerId).first()
            if answerObj == None or answerObj.questionId != questionObj.id:
                return "Invalid"
            if answerObj.correctAnswer: numCorrect += 1
        userResults = UserResult.query.filter_by(userid = session['user_id']).first()
        if userResults == None: 
            return "Invalid User"
        #TODO check if quiz has already been done
        oldQuizResult = QuizResult.query.filter_by(userresultid=userResults.id).first()
        if oldQuizResult != None:
            return "Quiz already completed"
        quizResult = QuizResult(quizid=quizId, userresultid=userResults.id, score=numCorrect)
        db.session.add(quizResult)
        db.session.commit()
        userResults = UserResult.query.filter_by(userid=session['user_id']).first()
        print("Success")
        return "Success"

#Login/Registration
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: 
        session['user_id'] = current_user.id
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user == None or not user.check_password(form.password.data): return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        session['user_id'] = user.id
        return redirect(url_for('index'))
    return render_template('Login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        #Todo check if refreshing works
        #Create results record for user
        userResults = UserResult(userid = User.query.filter_by(username=form.username.data).first().id)
        db.session.add(userResults)
        db.session.commit()
        #user.load_debug_user()
        return redirect(url_for('login'))
    return render_template('Registration.html', title='Registration', form=form)



