#!/usr/bin/python3
"""My list"""


class MyList(list):
    """class MyList"""

    def print_sorted(self):
        """prints the list (sorted)"""
        print(sorted(self))
