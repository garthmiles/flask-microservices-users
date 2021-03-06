# imports - 3rd-party modules
from flask_testing import TestCase
# imports - local modules
from project import create_app, db 

# instantiate the app 
app = create_app()

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app 
    
    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        