#!/usr/bin/python3
"""Add Attribute"""


def add_attribute(obj, att, value):
    """adds new attribute to an object if it’s applicable"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
