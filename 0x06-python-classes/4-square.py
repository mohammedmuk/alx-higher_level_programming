#!/usr/bin/python3

""" Define Square class """


class Square:

    """ Square class """

    def __init__(self, size=0):
        """ init constractor
            Args:
            param1: size
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")

        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        self.__size = value