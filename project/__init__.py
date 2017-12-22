# import core modules
import os 
import sys  
# import 3rd-party modules
from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)
# print(app.config, file=sys.stderr)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': "success",
        'message': "pong!"
})