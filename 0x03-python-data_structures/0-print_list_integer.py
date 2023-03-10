#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for li in my_list:
        if type(li) == int:
            print("{}".format(li))
