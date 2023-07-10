#!/usr/bin/python3
"""My Int"""


class MyInt(int):
    """invert operators"""

    def __eq__(self, operator):
        """invert operator (==) with (!=)"""
        return int(self) != operator

    def __ne__(self, operator):
        """invert operator (!=) with (==)"""
        return int(self) == operator
