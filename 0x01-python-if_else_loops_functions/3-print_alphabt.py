#!/usr/bin/python3
values = range(97, 123)

for value in values:
    if value != 101 and value != 113:
        print("{:s}".format(chr(value)), end="")
