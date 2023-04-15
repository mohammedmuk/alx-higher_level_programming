#!/usr/bin/python3

"""This is module to from_json_string function"""
import json


def from_json_string(my_str):
    """This is function convert json to python data"""

    py_data = json.loads(my_str)
    return py_data
