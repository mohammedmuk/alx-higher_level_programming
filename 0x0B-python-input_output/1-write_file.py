#!/usr/bin/python3
"""This is module for write_file function"""


def write_file(filename="", text=""):
    """This is function for write a text on file"""

    with open(filename, "w", encoding="utf-8") as f:
        write_data = f.write(text)
    return write_data
