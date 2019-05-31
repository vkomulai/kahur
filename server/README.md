# Raspberry PI Tennis ball machine Controller

- Two high torque 12V DC-motors and motor controllers
- One 12V dc motor to control ball feed

## Setting up raspberry PI for bluetooth ()

```sh
sudo apt-get update
sudo apt-get upgrade
sudo apt-get -y install build-essential bluetooth blueman bluez python-bluetooth libzbar-dev libzbar0 python-dev git scons swig libbluetooth-dev

sudo vim /lib/systemd/system/bluetooth.service
ExecStart=/usr/lib/bluetooth/bluetoothd -C

sudo systemctl daemon-reload
sudo service bluetooth restart

test connection
sudo python /usr/share/doc/python-bluez/examples/simple/rfcomm-server.py

expect to see Waiting for connection on RFCOMM channel 1
```

### Run the http emulator for simple local development

```sh
pip install -r requirements.txt
env BASIC_AUTH_USERNAME=your-username BASIC_AUTH_PASSWORD=your-pasword python startServer.py -h
```

## TODO

- GPIO: handle motors controlling ball speed and spin
- GPIO: handle motor contorlling ball feed interval
- Save state to disk
- Reset state / erate state
- Test with real hardware :smile:
