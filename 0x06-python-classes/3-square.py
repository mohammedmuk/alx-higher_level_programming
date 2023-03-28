#!/usr/bin/python3

""" Define Square class """


class Square:

    """ square class """
    def __init__(self, size=0):

        """ init constractor
            Args:
            pram1: size
        """

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
