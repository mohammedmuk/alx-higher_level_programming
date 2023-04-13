

"""This is module for inherits_from function"""


def inherits_from(obj, a_class):

    """This is function inherits_from"""

    if type(obj) is not a_class:
        return True
    else:
        return False

# a = True

# if inherits_from(a, int):
#     print("{} inherited from class {}".format(a, int.__name__))
# if inherits_from(a, bool):
#     print("{} inherited from class {}".format(a, bool.__name__))
# if inherits_from(a, object):
#     print("{} inherited from class {}".format(a, object.__name__))

print()