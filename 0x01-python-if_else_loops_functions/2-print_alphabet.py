#!/usr/bin/python3
values = range(97, 123)
for value in values:
    if value == 122:
        print(f"{chr(value)}")
        break

    print(f"{chr(value)}", end = "")

