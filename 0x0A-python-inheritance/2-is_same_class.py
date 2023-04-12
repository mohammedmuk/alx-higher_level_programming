#!/usr/bin/python3

"""This is module for is_same_class"""


def is_same_class(obj, a_class):
    """This function cheack if obj is instanse in class"""

    if type(obj) == a_class:
        return True
    else:
        return False
