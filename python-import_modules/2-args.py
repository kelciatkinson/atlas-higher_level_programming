#!/usr/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("{} argument:".format(len(sys.argv)))
        for i in sys.argv:
            print("{}: {}".format(len(sys.argv), i))
    else:
        print("{} arguments:".format(len(sys.argv)))
        for i in sys.argv:
            print("{}: {}".format(len(sys.argv), i))