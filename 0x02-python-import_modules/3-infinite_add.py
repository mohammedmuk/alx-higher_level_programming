#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = 0
    num2 = 1
    while len(argv) > num2:
        num += int(argv[num2])
        num2 += 1
    print("{}".format(num))
