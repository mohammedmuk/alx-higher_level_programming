#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = 1
    if len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    elif len(argv) > 1:
        if len(argv) == 2:
            print("{} argument:".format(len(argv) - 1))
        else:
            print("{} arguments:".format(len(argv) - 1))
        while len(argv) > num:
            print("{}: {}".format(num, argv[num]))
            num += 1
