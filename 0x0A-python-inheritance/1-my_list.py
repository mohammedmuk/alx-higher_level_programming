#!/usr/bin/python3


class MyList(list):
    """This is MyList Class"""

    def print_sorted(self):
        for i in self:
            int(i)
        self.sort()
        print(self)
