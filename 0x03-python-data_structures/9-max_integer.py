#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = 0
    if len(my_list) == 0:
        return None
    for li in my_list:
        if li > max_num:
            max_num = li
    return max_num
