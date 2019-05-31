#######################################
# HTTP Server for development purposes
# NOT meant to be used in production!!
#######################################

import os
from flask import Flask
from flask_basicauth import BasicAuth

import bluetoothControl
import systemControl
import gpioControl

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
    print("_listenClient, recieved command:", command)
    if command.startswith(systemControl.CMD_PREFIX):
        systemControl.handleSystem(command)
    elif command.startswith(gpioControl.CMD_PREFIX):
        gpioControl.handleBallFeeder(command)
    else:
        print('_listenClient, Unknown command:', command)
    return "Command:" + command


@app.route('/api/state', methods=['GET'])
def state():
    return gpioControl.getState().toJSON()
