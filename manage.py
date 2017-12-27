# imports - 3rd-party modules
from flask_script import Manager
# imports - local modules
from project import app, db 

# instantiate the app
mgr = Manager(app)

@mgr.command
def recreate_db():
    """recreates the db"""
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    """
    creates a new 'Manager' instance to handle all of the
    manager commands rec'd from the command line
    """
    mgr.run()
