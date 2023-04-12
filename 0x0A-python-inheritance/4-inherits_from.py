#!/usr/bin/python3

"""This is module for inherits_from function"""


def inherits_from(obj, a_class):

    """This is function inherits_from"""

    if type(obj) is not a_class:
        return True
    else:
        return False
