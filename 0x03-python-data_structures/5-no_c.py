#!/usr/bin/python3
def no_c(my_string):
    for st in my_string:
        if st == "c":
            table = my_string.maketrans("c", " ")
            my_string.translate(table)
            return my_string
        elif st == "C":
            table = my_string.maketrans("C", " ")
            my_string.translate(table)
            return my_string
