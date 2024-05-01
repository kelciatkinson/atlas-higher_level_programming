#!/usr/bin/python3

import sys

if __name__ == "__main__":
    number_of_arg = len(sys.argv) - 1
    if number_of_arg == 1:
        print("{} argument:".format(number_of_arg))
        print("{}: {}".format((number_of_arg), sys.argv[1]))
    else:
        print("{} arguments:".format(number_of_arg))
        for i in range(len(sys.argv)):
            if i > 0:
                print("{}: {}".format((i), sys.argv[i]))
            else:
                print("{}: {}".format((i), sys.argv[i]))
