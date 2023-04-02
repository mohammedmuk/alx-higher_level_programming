#!/usr/bin/python3

""" Define Square class """


class Square:
    """ Square class """
    def __init__(self, size=0):
        """ init constractor
            Args:
            pram1: size
        """
        self.__size = size

    @property
    def size(self):
        """ size publci method 
            
            Return: self.__size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size public method and called setter """
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Area Square method 

            Return: size * size
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ my_print Method """
        i = 0
        y = 0
        while i < self.__size:
            if self.__size == 0:
                print("")
                break
            while y < self.__size:
                print("#", end="")
                y += 1
            print("")
            i += 1

