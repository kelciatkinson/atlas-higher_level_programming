#!/usr/bin/python3

import sys

if __name__ == "__main__":
    number_of_arg = len(sys.argv) - 1
    if number_of_arg == 0:
        print(number_of_arg)
    elif number_of_arg == 1:
        print(sys.argv[number_of_arg])
    else:
        result = 0
        for i in range(1, len(sys.argv)):
            result = result + int(sys.argv[i])
        print(result)
