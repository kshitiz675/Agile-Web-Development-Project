import unittest
import os 

from app import app, db, priceloader
from app.models import User, Quiz, Topic, QuizResult, UserResult
from config import basedir

class UserModelCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_password_hashing(self):

        # TEST FOR USER 1
        u = User(username = 'john', email = 'john@gmail.com')
        u.set_password('123456')
        
        self.assertFalse(u.check_password('654321'))
        self.assertTrue(u.check_password('123456'))

       # TEST FOR USER 2
        v = User(username = 'tom', email = 'tom@gmail.com')
        v.set_password('helloworld')
        
        self.assertFalse(v.check_password('worldhello'))
        self.assertTrue(v.check_password('helloworld'))

    def test_database_seed(self):

        lesson = Topic.query.filter_by(topicname='The Blockchain').first()
        self.assertTrue(lesson.topicname == 'The Blockchain')

    def test_price_loader(self):
        loader = priceloader.PriceLoader()
        data = loader.getPriceData()
        self.assertTrue(len(data) == 10)

    def test_quiz_submission(self):
        #Create a quiz and make sure user result is updated when quiz is submitted

        user = User(username='Test', email='Test')
        user.set_password('Test')

        db.session.add(user)
        db.session.commit()

        userResult = UserResult(userid=user.id)
        db.session.add(userResult)
        db.session.commit()
        userid = UserResult.query.filter_by(userid=user.id).first().id

        quiz = Quiz(quizname='The Test')
        db.session.add(quiz)
        db.session.commit()
        
        db.session.add(QuizResult(quizid=quiz.id, userresultid=userid, score=2))

        db.session.commit()

        quizResult = UserResult.query.filter_by(userid=user.id).first().quizresults[0]
        self.assertTrue(quizResult.score == 2)

    def test_quiz_statistics_rank_correctly(self):

        user = User(username='Test 2', email='Test 2')
        user.set_password('Test2')

        db.session.add(user)
        db.session.commit()

        userResult = UserResult(userid=user.id)
        db.session.add(userResult)
        db.session.commit()
        userid = UserResult.query.filter_by(userid=user.id).first().id

        quiz = Quiz(quizname='The Test')
        db.session.add(quiz)
        db.session.commit()
        db.session.add(QuizResult(quizid=quiz.id, userresultid=userid, score=4))

        db.session.commit()

        self.assertTrue(QuizResult.getResultsForQuiz(quiz.id)[0][1] == 4)
    
if __name__=='__main__':
    unittest.main(verbosity=2)
