#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for fr_mt in matrix:
        for sc_mt in matrix[matrix.index(fr_mt)]:
            print("{:d} ".format(sc_mt), end='')
        print()
