from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(128))
    userresults = db.relationship('UserResult', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quizname = db.Column(db.String(128))
    questions = db.relationship('Question', backref='quiz', lazy=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questiontext = db.Column(db.String(256))
    quizId = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    answers = db.relationship('Answer', backref='question', lazy=True)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answertext = db.Column(db.String(256))
    questionId = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    correctAnswer = db.Column(db.Boolean)

class UserResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quizresults = db.relationship('QuizResult', backref='user_result', lazy=True)

class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quizid = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    userresultid = db.Column(db.Integer, db.ForeignKey('user_result.id'), nullable=False)
    score = db.Column(db.Integer)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))








	
	
