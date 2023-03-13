#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) < 2:
        if len(tuple_b) < 1:
            tuple_b = (0, 0)
        else:
            li = list(tuple_b)
            li.append(0)
            tuple_b = tuple(li)
    elif len(tuple_b) > 2:
        tuple_b = tuple_b[:2]
    new = tuple(map(sum, zip(tuple_a, tuple_b)))
    return new
