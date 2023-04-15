#!/usr/bin/python3

"""This is module for to_json_string function"""
import json


def to_json_string(my_obj):
    """This is function to convert object to json"""

    my_json = json.dumps(my_obj)
    return my_json
