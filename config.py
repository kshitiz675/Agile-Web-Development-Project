
import os
    #SQLite Configuration
    #TODO should we even use an ENV variable
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'cryptoquiz.db')
    
SQLALCHEMY_TRACK_MODIFICATIONS = False



