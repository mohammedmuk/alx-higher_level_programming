#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for fr_mt in matrix:
        for sc_mt in fr_mt:
            if fr_mt.index(sc_mt) == 2:
                print("{:d}".format(sc_mt), end='')
            else:
                print("{:d} ".format(sc_mt), end='')
        print()
