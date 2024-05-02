#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    backwards_list = my_list[-1::-1]
    for i in range(len(backwards_list)):
        print("{}".format(backwards_list[i]))
