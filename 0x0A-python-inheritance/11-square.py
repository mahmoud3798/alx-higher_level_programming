#!/usr/bin/python3
"""Square from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """instance from square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """method to print the square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)

    def area(self):
        """calc the area of the square"""
        return self.__size ** 2
