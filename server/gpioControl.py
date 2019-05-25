import json
# TODO: handle gpio

CMD_PREFIX = "BALL_FEED_"

CMD_PREFIX_SPEED = "SPEED_"
CMD_PREFIX_SPIN = "SPIN_"

CMD_START = "START"
CMD_STOP = "STOP"

CMD_SPEED_SLOW = "SLOW"
CMD_SPEED_FAST = "FAST"

CMD_SPIN_FLAT = "FLAT"
CMD_SPIN_TOP = "TOP"
CMD_SPIN_SLICE = "SLICE"


class State:
    def __init__(self, running, speed, spin):
        self.running = running
        self.speed = speed
        self.spin = spin

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=2)


state = State(CMD_STOP, CMD_SPEED_SLOW, CMD_SPIN_FLAT)


def getState():
    return state


def handleBallFeeder(command):
    cmd = command.replace(CMD_PREFIX, '')
    print('handleBallFeeder, command:', cmd)
    if cmd == CMD_START:
        _start()
    elif cmd == CMD_STOP:
        _stop()
    elif cmd.starsWith(CMD_PREFIX_SPEED):
        speed = command.replace(CMD_PREFIX_SPEED, '')
        _changeBallSeed(speed)
    elif cmd.starsWith(CMD_PREFIX_SPIN):
        spin = command.replace(CMD_PREFIX_SPIN, '')
        _changeBallSpin(spin)
    else:
        print('unknown command, cmd:', cmd)


def _stop():
    print('stopping ball feeder')
    state.running = CMD_STOP


def _start():
    print('Starting ball feeder')
    state.running = CMD_START


def _changeBallSpin(spin):
    print('Set ball spin:', spin)
    state.spin = spin


def _changeBallSeed(speed):
    print('Set ball speed:', speed)
    state.speed = speed
