#!/usr/bin/python3
# 1-square.py by Obed Boakye
"""Module for Square class. This module provides a simple
Square class with initialization based on size."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
