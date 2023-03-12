#!/usr/bin/python3
def no_c(my_string):
    for st in my_string:
        if st == "c":
            st = None
        elif st == "C":
            st = None
        return my_string
