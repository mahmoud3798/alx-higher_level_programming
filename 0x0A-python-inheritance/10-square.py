#!/usr/bin/python3
"""Square from Rectanfle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square"""

    def __init__(self, size):
        """instance from square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
