#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while i < x:
        if type(my_list[i]) is not int:
            continue
        print(my_list[i], end="")
        i += 1
    print()
    return x
