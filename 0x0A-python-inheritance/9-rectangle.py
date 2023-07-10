#!/usr/bin/python3
"""Base Geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        """instance from rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """method to print the rectangle"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

    def area(self):
        """calc the area of the retangle"""
        return self.__width * self.__height
