#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list)-1:
        return my_list
    else:
        new_list = my_list.copy()
        new_list.insert(idx, element)
        new_list.pop(idx+1)
        return new_list
