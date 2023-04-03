#!/usr/bin/python3

""" This is for Rectancle class with 2 Getter and 2 Setter"""


class Rectangle:
    """This is empty Rectangle class with pass"""

    def __init__(self, width=0, height=0):
        """ init function """

        self.__height = height
        self.__width = width

    @property
    def height(self):
        """ Getter function
            Return: self.__height"""

        return self.__height

    @property
    def width(self):
        """ Getter function
            Return: self.__width"""

        return self.__width

    @width.setter
    def width(self, value):
        """ Setter function make apdate to width to new value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Setter function make apdate to height to new value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
