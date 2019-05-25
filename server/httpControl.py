#######################################
# HTTP Server for development purposes
# NOT meant to be used in production!!
#######################################

import bluetoothControl
import gpioControl
import os
from flask import Flask
from flask_basicauth import BasicAuth


app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.environ.get(
    'BASIC_AUTH_USERNAME', 'user')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get(
    'BASIC_AUTH_PASSWORD', 'pwd')
app.config['BASIC_AUTH_FORCE'] = True   # All routes require auth
basic_auth = BasicAuth(app)


def listen():
    app.run(debug=True)
    print("httpControl, listen")


@app.route('/api/control/<string:command>', methods=['POST'])
def control(command):
    bluetoothControl._handleInputData(command)
    return "Command:" + command


@app.route('/api/state', methods=['GET'])
def state():
    return gpioControl.getState().toJSON()
