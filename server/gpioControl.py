# TODO: handle gpio

CMD_PREFIX = "BALL_FEED_"

CMD_PREFIX_SPEED = "SPEED_"
CMD_PREFIX_SPIN = "SPIN_"

CMD_START = "START"
CMD_STOP = "STOP"


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


def _start():
    print('Starting ball feeder')


def _changeBallSpin(spin):
    print('Set ball spin:', spin)


def _changeBallSeed(speed):
    print('Set ball speed:', speed)
