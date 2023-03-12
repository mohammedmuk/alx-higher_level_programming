#!/usr/bin/python3
def element_at(my_list, idx):
    num_list = len(my_list) - 1
    if idx < 0:
        return None
    elif idx > num_list:
        return None
    else:
        return my_list[idx]
