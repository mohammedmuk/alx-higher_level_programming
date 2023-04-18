#!/usr/bin/python3
"""This is module for Rectangle Class"""

from base import Base


class Rectangle(Base):
    """This is class for height and width and x and y attribute"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def hight(self, value):
        self.__height = value
