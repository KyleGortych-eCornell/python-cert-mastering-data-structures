"""
funcs
Descript:


File name:     funcs.py
Maintainer:    Kyle Gortych
Created:       06-14-2022
Last Modified: 07-22-2022
"""

def clamp(alist,min,max):
    """
    Modifies alist so that every element is between min and max.

    Any number in the list less than min is replaced with min.  Any number
    in the tuple greater than max is replaced with max. Any number between
    min and max is left unchanged.

    Examples:
        If a = [-1, 1, 3, 5], clamp(a,0,4) changes a to [0,1,3,4]
        If a = [-1, 1, 3, 5], clamp(a,-2,8) changes a to [-1,1,3,-5]
        If a = [-1, 1, 3, 5], clamp(a,-2,-1) changes a to [-1,-1,-1,-1]
        If a = [], clamp(a,0,4) returns []

    Parameter alist: the list to modify
    Precondition: alist is a list of numbers (float or int)

    Parameter min: the minimum value for the list
    Precondition: min <= max is a number

    Parameter max: the maximum value for the list
    Precondition: max >= min is a number
    """
    assert (isinstance(alist, list) and 
            all(isinstance(item, (int, float)) for item in alist))
    assert isinstance(min, (int, float)) and min <= max
    assert isinstance(max, (int, float)) and max >= min

    # Modify original param alist
    # Procedure no return

    for idx in range(len(alist)):
        if alist[idx] < min:
            alist[idx] = min
        if alist[idx] > max:
            alist[idx] = max

    #pass

def removeall(alist,n):
    """
    Removes all instances of n from alist

    Examples:
        If a = [1,2,2,3,1], removeall(a,1) changes a to [2,2,3]
        If a = [1,2,2,3,1], removeall(a,2) changes a to [1,3,1]
        If a = [1,2,2,3,1], removeall(a,4) changes a to [1,2,2,3,1]
        If a = [1,1,1], removeall(a,1) changes a to []
        If a = [], removeall(a,1) changes a to []

    Parameter alist: the list to modify
    Precondition: alist is a list of numbers (float or int)

    Parameter n: the number to remove
    Precondition: n is a number
    """
    assert (isinstance(alist, list) and 
            all(isinstance(item, (int, float)) for item in alist))
    assert isinstance(n, (int, float))

    #Modify original param alist

    acc = alist.count(n)

    for idx in range(acc):
        alist.remove(n)

    #pass
