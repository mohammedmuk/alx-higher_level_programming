#!/usr/bin/python3
"""This is module for is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """This function cheack if obj is instance in class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
