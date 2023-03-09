#!/usr/bin/python3
values = range(0, 100)

for value in values:
    if value == 99:
        print("{:d}\n".format(value))
        break
    print("{:d}, ".format(str(value).zfill(2)))
