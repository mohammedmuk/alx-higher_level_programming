#!/usr/bin/python3

"""This is module for BaseGeometry"""


class BaseGeometry:
    """This is an class raise Error"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """This is Rectangle class"""
    def __init__(self, width, height):
        Rectangle.integer_validator(self, "height", height)
        Rectangle.integer_validator(self, "width", width)
        self.__height = height
        self.__width = width
