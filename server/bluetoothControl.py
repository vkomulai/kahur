# Importing the Bluetooth Socket library
import bluetooth
import sys
import systemControl
from systemControl import *
import gpioControl
from gpioControl import *


def listen():
    try:
        client, server = _connect()
    except:
        print("Bluetooth Binding Failed, exiting")
        sys.exit(1)

    try:
        _listenClient(client)
    except:
        client.close()
        server.close()
        print("Bluetooth done")


def _connect():
    ONE_CONNECTION_AT_TIME = 1
    host = ""
    port = 1
    server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    print('Bluetooth Socket Created')

    server.bind((host, port))
    server.listen(ONE_CONNECTION_AT_TIME)
    client, address = server.accept()
    print("Connected To", address)
    print("Client:", client)
    print("Bluetooth Binding Completed")
    return client, server


def _listenClient(client):
    while True:
        data = client.recv(1024)  # 1024 is the buffer size.
        print("_listenClient, recieved data:", data)
        if data.startswith(systemControl.CMD_PREFIX):
            systemControl.handleSystem(data)
        elif data.startswith(gpioControl.CMD_PREFIX):
            gpioControl.handleBallFeeder(data)
        else:
            print('_listenClient, Unknown command:', data)
