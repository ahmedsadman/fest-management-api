import os

class Config:
    '''holds all the configuration for the flask application'''
    
    # general config
    SECRET_KEY = 'mysecretkeytest'
    PROPAGATE_EXCEPTIONS = True
    
    # database
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'sqlite:///data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
