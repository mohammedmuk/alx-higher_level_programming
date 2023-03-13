#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        print("")
        return None
    num = len(my_list) - 1
    while num >= 0:
        print("{:d}".format(my_list[num]))
        num -= 1
