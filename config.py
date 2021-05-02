
import os
<<<<<<< HEAD

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
=======
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    #SQLite Configuration
    #TODO should we even use an ENV variable
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'cryptoquiz.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False



>>>>>>> 033bd819416ae28744c3b999765b8fa327fdb51e
