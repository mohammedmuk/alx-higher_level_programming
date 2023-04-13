#!/usr/bin/python3

"""This is module for MyList class"""


class MyList(list):
    """This is MyList Class"""

    def print_sorted(self):
        for i in self:
            if type(i) is not int:
                self[self.index(i)] = int(i)
        li = self.copy()
        li.sort()
        print(li)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
