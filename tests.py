import unittest

from app import app, db
from app.models import User, Quiz

class UserModelCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
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


        


    def test_quiz_model(self):
        #, questions = ['this is a question','this is another question']

        u1 = User(username = 'jake', email = 'jake@gmail.com')
        u1.set_password('jake123')
        db.session.add(u1)
        db.session.commit()


        #quiz = Quiz.query.filter_by(id=1).first()
        self.assertEqual(Quiz.quizname, 'The Blockchain')

        q1 = Quiz(quizname = 'Question 1')

        self.assertTrue(v.check_password('helloworld'))


        #self.assertFalse(q1.get_questions(['this is a questions','this is another questions']))
        #self.assertTrue(q1.get_questions(['this is a question','this is another question']))

        

if __name__=='__main__':
    unittest.main(verbosity=2)
