import os
basedir = os.path.abspath(os.path.dirname(__file__)) # Tell python to look at all files same on ANY operating system

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You_will_never_guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATION = False