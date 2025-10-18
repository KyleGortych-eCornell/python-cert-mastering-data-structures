"""
Module to demonstrate tuple expansion.

Maintainer: Kyle Gortych
Date:       07-23-2022
"""

def avg(*args):
    """
    Returns average of all of arguments (passed via tuple expansion)
    
    Remember that the average of a list of arguments is the sum of all of the elements 
    divided by the number of elements.
    
    Examples: 
        avg(1.0, 2.0, 3.0) returns 2.0
        avg(1.0, 1.0, 3.0, 5.0) returns 2.5
    
    Parameter args: the function arguments
    Precondition: args are all numbers (int or float)
    """
    assert (isinstance(args, tuple) and 
            all(isinstance(item, (int, float)) for item in args))

    if len(args) == 0:
        return 0
        
    return sum(args[:]) / len(args)

    # pass
