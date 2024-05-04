#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = my_list.copy()
    new_list = list(map(lambda x: x * number, (i for i in new_list)))
    return new_list
