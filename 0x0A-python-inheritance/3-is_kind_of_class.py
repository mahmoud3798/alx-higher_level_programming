#!/usr/bin/python3
"""is kind of class"""


def is_kind_of_class(obj, a_class):
    """check whether an object is an instance of, or if the object is an instance
    of a class that inherited from"""

    return (isinstance(obj, a_class) or issubclass(type(obj), a_class))
