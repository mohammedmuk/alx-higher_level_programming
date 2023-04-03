#!/usr/bin/python3

""" This is for Rectancle class with 2 Getter and 2 Setter"""


class Rectangle:
    """This is empty Rectangle class with pass"""

    def __init__(self, width=0, height=0):
        """ init function """

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ Getter function
            Return: self.__width"""
        if type(self.__width) != int:
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        else:
            return self.__width

    @width.setter
    def width(self, value):
        """ Setter function make apdate to width to new value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter function
            Return: self.__height"""
        if type(self.__height) != int:
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")
        else:
            return self.__height

    @height.setter
    def height(self, value):
        """ Setter function make apdate to height to new value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
