#!/usr/bin/python3

""" This is for Rectancle class with 2 Getter and 2 Setter"""


class Rectangle:
    """This is empty Rectangle class with pass"""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ init function """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter function
            Return: self.__width"""

        return self.__width

    @width.setter
    def width(self, value):
        """ Setter function make apdate to width to new value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter function
            Return: self.__height"""

        return self.__height

    @height.setter
    def height(self, value):
        """ Setter function make apdate to height to new value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        h = 0
        w = 0
        st = ""
        if self.__height == 0 or self.__width == 0:
            return st
        while h < self.__height:
            w = 0
            while w < self.__width:
                st += str(self.print_symbol)
                w += 1
            if h == self.__height - 1:
                return st
            st += "\n"
            h += 1
        return st

    def __print__(self):
        h = 0
        w = 9
        if self.__height == 0 or self.__width == 0:
            return ""
        while h < self.__height:
            w = 0
            while w < self.__width:
                print(f"{self.print_symbol}", end="")
                w += 1
            if h == self.__height - 1:
                break
            print("")
            h += 1

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
