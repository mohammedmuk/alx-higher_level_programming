#!/usr/bin/python3


def max_integer(my_list=[]):
    """ find the max number in list """

    if len(my_list) == 0:
        return None

    max_num = my_list[0]

    for li in my_list:
        if li > max_num:
            max_num = li
    return int(max_num)
