import subprocess

CMD_PREFIX = 'SYSTEM_'


def handleSystem(data):
    _shutdown(True)


def _shutdown(simulate=True):
    command = "/usr/bin/sudo ls -la" if simulate else "/usr/bin/sudo /sbin/shutdown now"
    print "Executing command [" + command + "]"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output


if __name__ == '__main__':
    _shutdown()
