"""
Module to demonstrate functions on nested dictionaries.

This module uses the data in the file 'weather.json'. This module does not need to
worry about reading and opening the file -- test.py does that.  However, you should
look at that file to familiarize your self with the data format.

In that file weather is a dictionary whose keys are timestamps (year,month,day,hour,etc.)
and whose values are weather reports. The contents of interest in this module is the nested "temperature" dictionary.

IMPORTANT: Not all weather reports contain a temperature measurement.

Author: Kyle Gortych
Date: 08-02-2022
"""
import copy

# Helper to use in function below
def to_celsius(x):
    """
    Returns x converted to celsius

    The value returned has type float.

    Parameter x: the temperature in fahrenheit
    Precondition: x is a number
    """
    return 5*(x-32)/9.0


# Implement this function
def reports_above_temp(weather,temp):
    """
    Returns the number of weather reports where temperature is above temp (in Celsius)

    The parameter weather contains a weather report dictionary.  This function loops
    through the weather reports and counts all reports for which
    (1) the report has a temperature measurement (not all reports do)
    (2) the measured temperature is properly above temp in Celsius

    A temperature measurement is itself a dictionary with two keys: 'value' and 'units'.
    For example:

        "temperature": {
            "value": 57.0,
            "units": "F"
        }

    The units are always either 'F' for fahrenheit or 'C' for celsius.  If the
    measurement is in fahrenheit, the value will need to be converted before it
    can be compared to temp.

    Parameter weather: the weather dictionary
    Precondition: weather has the format described in the module introduction

    Parameter temp: the temperature in celsius
    Precondition: temp is an int or float
    """
    # assert isinstance(weather.method(), type)
    # assert isinstance(temp, (int, float))
    c = copy.deepcopy(weather)
    result = 0
    for report in c.keys():
        if 'temperature' in c[report]:
            if c[report]['temperature']['units'] == 'F':
                c[report]['temperature']['value'] = to_celsius(c[report]['temperature']['value'])
            if c[report]['temperature']['value'] > temp:
                result += 1
    return result
    #pass
