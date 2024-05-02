#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = 0
    
    new_tuple = (tuple_a[i] + tuple_b[i], tuple_a[i+1] + tuple_b[i+1])
    return new_tuple
