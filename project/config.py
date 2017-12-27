
# imports - core modules
import os 
# imports - 3rd-party modules
from dotenv import load_dotenv, find_dotenv

# load local 'env' variables
load_dotenv(find_dotenv())
SECRET = os.environ.get('SECRET_KEY')

class BaseConfig:
    global SECRET 
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SECRET_KEY = SECRET



class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

