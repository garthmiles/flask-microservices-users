# imports - core modules
import unittest 
# imports - 3rd-party modules
from flask import current_app
from flask_testing import TestCase
# imports - local modules
from project import app 

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.DevelopmentConfig')
        return app 

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')