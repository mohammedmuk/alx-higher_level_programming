#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    num_list = len(my_list) - 1
    if idx < 0:
        return my_list
    elif idx > num_list:
        return my_list
    else:
        my_list[idx] = element
        return my_list
