#!/usr/bin/python3
"""This module defines the save_to_json_file function"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
new_list = []
load_from_json_file(filename)
save_to_json_file(new_list, filename)
