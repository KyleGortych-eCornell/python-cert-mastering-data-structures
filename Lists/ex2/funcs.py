"""
funcs
Descript:


File name:     funcs.py
Maintainer:    Kyle Gortych
Created:       06-10-2022
Last Modified: 06-12-2022
"""

def clamp(alist,min,max):
    """
    Returns a copy of alist where every element is between min and max.

    Any number in the list less than min is replaced with min.  Any number
    in the tuple greater than max is replaced with max. Any number between
    min and max is left unchanged.

    Examples:
        clamp([-1, 1, 3, 5],0,4) returns [0,1,3,4]
        clamp([-1, 1, 3, 5],-2,8) returns [-1,1,3,-5]
        clamp([-1, 1, 3, 5],-2,-1) returns [-1,-1,-1,-1]
        clamp([],0,4) returns []

    Parameter alist: the list to copy
    Precondition: alist is a list of numbers (float or int)

    Parameter min: the minimum value for the list
    Precondition: min <= max is a number

    Parameter max: the maximum value for the list
    Precondition: max >= min is a number
    """
    assert all(isinstance(item, (int, float)) for item in alist)
    assert isinstance(min, (int, float))
    assert isinstance(max, (int, float))

    #do not modify original param alist

    result = []
    for value in alist:
        if value < min:
            result.append(min)
        if value > max:
            result.append(max)
        if value in range(min,max + 1):
            result.append(value)

    return result
    #pass


def removeall(alist,n):
    """
    Returns a copy of alist, removing all instances of n

    Examples:
        removeall([1,2,2,3,1],1) returns [2,2,3]
        removeall([1,2,2,3,1],2) returns [1,3,1]
        removeall([1,2,2,3,1],4) returns [1,2,2,3,1]
        removeall([1,1,1],1) returns []
        removeall([],1) returns []

    Parameter alist: the list to copy
    Precondition: alist is a list of numbers (float or int)

    Parameter n: the number to remove
    Precondition: n is a number
    """
    assert all(isinstance(value, (int, float)) for value in alist)
    assert isinstance(n, (int, float))

    #do not modify original param alist

    result = []
    [result.append(value) for value in alist if value != n]

    #result = []
    #for value in alist:
    #    if value != n:
    #        result = result.append(value)

    return result
    #pass

# Assess unit test

# fn1_test_case1 = clamp([-1,1,3,5],0,4)
# fn1_test_case2 = clamp([-1,1,3,5],-2,8)
# fn1_test_case3 = clamp([-1,1,3,5],-2,-1)
# fn1_test_case4 = clamp([],0,4)
#
# fn2_test_case1 = removeall([1,2,2,3,1],1)
# fn2_test_case2 = removeall([1,2,2,3,1],2)
# fn2_test_case3 = removeall([1,2,2,3,1],4)
# fn2_test_case4 = removeall([1,1,1],1)
# fn2_test_case4 = removeall([],1)
#
# print(
#     ''.join(['fn1_test_case1: ', str(fn1_test_case1)]),
#     ''.join(['\nfn1_test_case2: ', str(fn1_test_case2)]),
#     ''.join(['\nfn1_test_case3: ', str(fn1_test_case3)]),
#     ''.join(['\nfn1_test_case4: ', str(fn1_test_case4)]),
#     '\n',
#     ''.join(['\nfn2_test_case1: ', str(fn2_test_case1)]),
#     ''.join(['\nfn2_test_case2: ', str(fn2_test_case2)]),
#     ''.join(['\nfn2_test_case3: ', str(fn2_test_case3)]),
#     ''.join(['\nfn2_test_case4: ', str(fn2_test_case4)])
# )
