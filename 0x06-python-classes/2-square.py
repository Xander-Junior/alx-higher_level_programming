#!/usr/bin/python3
# 2-square.py by Obed Boakye
"""
Module for Square class. This module provides the Square class
which allows for initializing a square with size validation.
"""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square, with validation checks.
    """

    def __init__(self, size=0):
        """Initializes a new Square with size validation.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
