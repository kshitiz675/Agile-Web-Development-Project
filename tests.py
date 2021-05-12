import unittest

from app import app, db
from app.models import User, QuizResult

class UserModelCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()



    def test_password_hashing(self):

        u = User(username = '1234')
        u.set_password('123456')
        
        self.assertFalse(u.check_password('654321'))
        self.assertTrue(u.check_password('123456'))


if __name__=='__main__':
    unittest.main(verbosity=2)
