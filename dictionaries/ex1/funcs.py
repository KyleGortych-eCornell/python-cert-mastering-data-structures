"""
Module demonstrating immutable functions on dictionaries

All of these functions make use of accumulators.

Author: Kyle Gortych
Date: 08/01/2022
"""
import copy

def average_grade(adict):
    """
    Returns the average grade among all students.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This function
    averages those grades and returns a value.

    Examples:
        average_grade({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns (55+90+86)/3 = 77
        average_grade({'wmw2' : 55}) returns 55
        average_grade({}) returns 0

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    #assert isinstance(adict, dict), "parameter not a dictionary"
    #assert isinstance(adict.keys(), str), "all keys must be str"
    #assert isinstance(adict.values(), int), "all values must be ints"
    if len(adict) > 0:
        return sum(adict.values()) / len(adict.values())
    return 0
    # pass

def letter_grades(adict):
    """
    Returns a new dictionary with the letter grades for each student.

    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam. This function returns a
    new dictionary with netids for keys and letter grades (strings) for values.

    Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for a D. Anything below 60
    is an F.

    Examples:
        letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns
            {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
        letter_grades({}) returns {}

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    #assert isinstance(adict, dict), "parameter not a dictionary"
    #assert isinstance(adict.keys(), str), "all keys must be str"
    #assert isinstance(adict.values(), int), "all values must be ints"
    #assert if len(adict) > 0:
    #    return {}

    c = copy.deepcopy(adict)
    if len(c) > 0:
        for key, value in c.items():
            if value > 89:
                c[key] = 'A'
            elif value > 79:
                c[key] = 'B'
            elif value > 69:
                c[key] = 'C'
            elif value > 59:
                c[key] = 'D'
            elif value <= 59:
                c[key] = 'F'
        return c
    return {}

    # pass
