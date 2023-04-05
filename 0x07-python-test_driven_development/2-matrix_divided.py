def matrix_divided(matrix, div):
    list_t = []
    num = 0
    if type(div) != int:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for first in matrix:
        list_s = []
        if first == matrix[0]:
            num += len(first)
        for second in first:
            if type(second) != int and type(second) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                list_s.append(float("{:.2f}".format(second / div)))

        if first != matrix[0]:
            if len(first) != num:
                raise TypeError("Each row of the matrix must have the same size")

        list_t.append(list_s)
    return list_t

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")