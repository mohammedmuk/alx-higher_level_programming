#!/usr/bin/python3

"""This is module for append_write"""


def append_write(filename="", text=""):
    """This is function for append new text"""

    with open("file_append.txt", "a+", encoding="utf-8") as f:
        write_data = f.write(text)
    return write_data
