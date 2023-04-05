#!/usr/bin/python3

"""
   This is module to add-integer function

   take two argument and sum it
"""


def add_integer(a, b=98):
    """ This is add_integer() function:
        Args(a, b):
        Return: a + b """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    num = int(a) + int(b)
    return num


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")