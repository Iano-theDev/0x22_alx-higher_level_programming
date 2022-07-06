#!/usr/bin/python3
'''
script that add all arguments to a python list, and saves them to a file
'''

from sys import argv
save_to_jason_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except:
    json_list = []

for arg in argv[1:]:
    json.list.append(arg)

save_to_jason_file(json_list, filename)
