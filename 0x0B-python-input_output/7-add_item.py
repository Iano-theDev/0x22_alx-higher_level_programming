#!/usr/bin/python3
'''
    adds all arguments to a python list,
    and saves the to a file
'''

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_to_json_file = __import__('6-load_from_json_file').save_to_json_file

filename = "add_item.json"


my_list = []
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    pass

my_list += sys.argv[1:]:
save_to_json_file(my_list, filename)
