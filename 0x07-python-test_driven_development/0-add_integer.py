

"""
   This is module to add-integer function

   take two argument and sum it
"""

def add_integer(a, b=98):
    """ This is add_integer() function:
        Args(a, b):
        Return: a + b """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)