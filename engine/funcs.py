#!/usr/bin/python3

"""
Here is the main functions that are doing some logic math operations
"""

def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
    """Division function"""
    if y == 0:
        return "Error! Division by zero is undefined."
    return x / y

def square(x):
    """Square function"""
    return x ** 2

def square_root(x):
    """Square root function"""
    if x < 0:
        return "Error! Square root of a negative number is undefined."
    return x ** 0.5
