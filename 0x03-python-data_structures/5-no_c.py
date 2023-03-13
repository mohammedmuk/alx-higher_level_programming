#!/usr/bin/python3
def no_c(my_string):
    li_str = []
    for i in my_string:
        if i != 'c' and i != 'C':
            li_str.append(i)

    string = "".join(li_str)
    return string
