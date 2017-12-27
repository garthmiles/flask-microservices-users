# imports - core modules
import unittest 
# imports - 3rd-party modules
from dotenv import find_dotenv, load_dotenv
from flask import current_app
from flask_testing import TestCase
# imports - local modules
from project import app 

# load local 'env' values
load_dotenv(find_dotenv())

# construct main db url string
DB_URI = f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@users-db:5432'

class TestDevelopmentConfig(TestCase):
    global DB_URI 
    def create_app(self):
        app.config.from_object('project.config.DevelopmentConfig')
        return app 

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == DB_URI + '/users_dev'
        )
    
class TestTestingConfig(TestCase):
    global DB_URI 
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app 

    def test_app_is_testing(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] == DB_URI + '/users_test')

class TestProductionConfig(self):
    global DB_URI
    def create_app(self):
        app.config.from_object('project.config.ProductionConfig')
        return app 

    def test_app_is_production(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])

if __name__ == '__main__':
    unittest.main()
    



