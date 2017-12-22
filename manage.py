# import 3rd-party modules
from flask_script import Manager
from project import app 

mgr = Manager(app)

if __name__ == '__main__':
    """
    creates a new 'Manager' instance to handle all of the
    manager commands rec'd from the command line
    """
    mgr.run()
