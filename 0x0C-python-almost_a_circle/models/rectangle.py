#!/usr/bin/python3
"""This is module for Rectangle Class"""

from base import Base


class Rectangle(Base):
    """This is class for height and width and x and y attribute"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This constractor consist main attribute"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def hight(self, value):
        """Height setter"""
        self.__height = value
