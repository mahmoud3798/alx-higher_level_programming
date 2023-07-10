#!/usr/bin/python3
"""is same class"""


def is_same_class(obj, a_class):
    """check whether an object is exactly an instance of a given class"""

    return (type(obj) is a_class)
