#!/usr/bin/python3
"""This is module for save_to_json_file function"""

import json


def save_to_json_file(my_obj, filename):
    """This is function to create and save json file"""

    json_data = json.dumps(my_obj)
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(json_data)
