# imports - core modules
import os 
# imports - 3rd-party modules
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy



# instantiate the db
db = SQLAlchemy()

def create_app():

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set-up extensions 
    db.init_app(app)

    # register blueprints
    from project.api.views import users_blueprint
    app.register_blueprint(users_blueprint)

    return app 


# db model
# class User(db.Model):
#     """define the table scheme"""
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(128), nullable=False)
#     email = db.Column(db.String(128), nullable=False)
#     active = db.Column(db.Boolean(), default=False, nullable=False)
#     created_at = db.Column(db.DateTime, nullable=False)

#     def __init__(self, username, email):
#         """initializes and exposes username, email, & created_at 
#         variables to the rest of the class
#         """
#         self.username = username
#         self.email = email 
#         self.created_at = datetime.datetime.utcnow()


# # app routes
# @app.route('/ping', methods=['GET'])
# def ping_pong():
#     return jsonify({
#         'status': "success",
#         'message': "pong!"
# })