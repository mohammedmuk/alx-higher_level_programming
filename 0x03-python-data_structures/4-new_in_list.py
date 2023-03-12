#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    num_list = len(my_list) - 1
    new_list = my_list.copy()

    if idx < 0:
        return new_list
    elif idx > num_list:
        return new_list
    else:
        new_list[idx] = element
        return new_list
