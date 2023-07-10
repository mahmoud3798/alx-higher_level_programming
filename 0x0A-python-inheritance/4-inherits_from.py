#!/usr/bin/python3
"""inherits from"""


def inherits_from(obj, a_class):
    """check whether an object is an instance of a class 
	that inherites from the specified class"""

    return (type(obj) is not a_class and issubclass(type(obj), a_class))
