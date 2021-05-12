from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import random

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
    
    def debug_hashpassword(self, password):
        return generate_password_hash(password)

    def load_debug_user(self):
        print("Loading Debug User")
        userresultid = UserResult.query.filter_by(userid=self.id).first().id
        db.session.add(QuizResult(quizid=3, userresultid=userresultid, score=2))
        db.session.add(QuizResult(quizid=2, userresultid=userresultid, score=1))
        db.session.commit()

        print(self.username + "Results")
        userResults = UserResult.query.filter_by(userid=self.id).first()
        for result in userResults.quizresults:
            quiz = Quiz.query.filter_by(id=result.quizid).first()
            print(quiz.quizname)
            print(f'{result.score} / {len(quiz.questions)}')
            print()

    


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quizname = db.Column(db.String(128))
    questions = db.relationship('Question', backref='quiz', lazy=True)

    'Return all questions that belong to the topic of this quiz'
    def get_questions(self):
        return Question.query.filter_by(quizId=self.id).all()
    'Return a specific question from a quiz'
    def get_a_question(self, num):
        return Question.query.filter_by(quizId=self.id, id=num).first()


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questiontext = db.Column(db.String(256))
    quizId = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    answers = db.relationship('Answer', backref='question', lazy=True)

    'Get all options for question'
    def get_answers(self):
        return Answer.query.filter_by(questionId=self.id).all()
    'Get a specific answer for a question'
    def get_a_answer(self, num):
        return Answer.query.filter_by(questionId=self.id, id=num).first()
    'Get correct answer'
    def get_correct_answer(self):
        return Answer.query.filter_by(questionId=self.id, correctAnswer=1).first()
    'Get question'
    def get_question(self):
        return self.questiontext
    def get_randomized_answers(self):
        answers = Answer.query.filter_by(questionId = self.id).all()
        random.shuffle(answers)
        return answers



class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answertext = db.Column(db.String(256))
    questionId = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    correctAnswer = db.Column(db.Boolean)

    def get_text(self):
        return self.answertext
    def check_correct(self):
        return self.correctAnswer

class UserResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quizresults = db.relationship('QuizResult', backref='user_result', lazy=True)


class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quizid = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    userresultid = db.Column(db.Integer, db.ForeignKey('user_result.id'), nullable=False)
    score = db.Column(db.Integer)

    def getBestResults(quizId, numResults):
        return QuizResult.query.filter_by(quizid = quizId).order_by(QuizResult.score).limit(numResults).all()

    def getResultsForAllQuizzes():
        results = []
        for quiz in Quiz.query.all():
            quizResults = QuizResult.getResultsForQuiz(quiz.id)
            results.append((quiz.quizname, quizResults))
        return results
    def getResultsForQuiz(quizId):
        results = []
        rank = 1
        for quizResult in QuizResult.query.filter_by(quizid=quizId).order_by(QuizResult.score.desc()).limit(10):
            userId = UserResult.query.filter_by(userid=quizResult.userresultid).first().userid
            username = User.query.filter_by(id=userId).first().username
            results.append((username, quizResult.score, rank))
            rank += 1
        return results
            
class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quizid = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=True)
    topicname = db.Column(db.String(256))
    topicvideolink = db.Column(db.String(256))
    topicsections = db.relationship('TopicSection', backref='topic', lazy=True)

class TopicSection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topicid = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    topicheading = db.Column(db.String(256))
    topiccontent = db.Column(db.String(1024))


##Login system
@login.user_loader
def load_user(id):
    return User.query.get(int(id))















	
	
