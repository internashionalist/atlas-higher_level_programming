#!/usr/bin/python3
"""
Module for add_item
"""
import sys
import json
import os

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

filename = "add_item.json"  # file to store list of arguments

try:
    j_list = load_from_json_file(filename)  # load list if file exists
except Exception:
    j_list = []  # create empty list if file does not exist

for arg in sys.argv[1:]:  # iterate through arguments from command line
    j_list.append(arg)  # add arguments to list

save_to_json_file(j_list, filename)  # save list of arguments to file
