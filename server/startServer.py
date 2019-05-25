#!/bin/env/python
import sys
import getopt
import bluetoothControl
import httpControl


def main(argv):
    try:
        opts, args = getopt.getopt(
            argv, "bh", ["mode-bluetooth", "mode-http"])
    except getopt.GetoptError:
        print('startServer.py -i <inputfile> -o <outputfile>')
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-b", "--mode-bluetooth"):
            bluetoothControl.listen()
        elif opt in ("-h", "--mode-http"):
            httpControl.listen()

    print("Tennisball machine running in:", opt)


if __name__ == "__main__":
    main(sys.argv[1:])
