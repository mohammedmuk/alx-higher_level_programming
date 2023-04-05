def print_square(size):
    """
    print_square:
    function return square shape if you put positive number in arrgument

    Return: no return
    """
    h = 0
    w = 0
    if type(size) is float:
        size = int(size)
    elif type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    while h < size:
        w = 0
        while w < size:
            print("#", end="")
            w += 1
        print("")
        h += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")