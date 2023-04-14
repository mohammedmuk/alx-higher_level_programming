#!/usr/bin/python3
"""This is module for read_file function"""


def read_file(filename=""):
    """This is function for print and read text file"""

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
