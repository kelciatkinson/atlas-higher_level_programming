#!/usr/bin/python3

def read_file(filename=""):
    with open("my_file_0.txt", "r") as f:
        f_contents = f.read()
        print(f_contents) 
