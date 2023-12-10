#!/usr/bin/python3

"""Decides that the given arithmetic expression is"""
from engine.funcs import *


def arithmetic_check(args):
    """executes the given arithmetic expression"""

    items =args.split()

    operand1= items[0]
    operator= items[1]
    operand2= items[2]

    try: 
        operand1 = int(operand1)
        operand2 = int(operand2)

    except ValueError:
        raise ValueError("Invalid operand")
    
    if operator == "+":
        return add(operand1, operand2)
    
    elif operator == "-":
        return subtract(operand1, operand2)
    
    elif operator == "*":
        return multiply(operand1, operand2)
    
    elif operator == "/":
        return divide(operand1, operand2)
    
    elif operator == "**":
        return square(operand1)
    
    elif operator == ")":
        return square_root(operand1)
    


    
