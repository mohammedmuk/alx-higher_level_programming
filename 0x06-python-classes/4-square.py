#!/usr/bin/python3
""" Create Square Class """


class Square:

    """ Square class """

    def __init__(self, size=0):
        """ init constractor
            Args:
            param1: size
        """
        self.__size = size

    @property
    def size(self):
        """ size is getter """

        return self.__size

    @size.setter
    def size(self, value):
        """ size for setter
            Args:
            pram1: value
        """
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Area in square class

            Return: Square Area
        """
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")

        return (self.__size * self.__size)
