#!/usr/bin/python3
'''
contains from_json_string function
'''

import json


def from_json_string(my_str):
    '''
    returns an object (Python data structure)
    represented by a JSON string
    '''
    return json.loads(my_str)
