#!/usr/bin/python3

"""This is module for BaseGeometry"""


class BaseGeometry:
    """This is an class raise Error"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        name = str(name)
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")