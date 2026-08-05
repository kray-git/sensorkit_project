"""
Module: sensorkit/stats.py
Contributor: Cyril Norgbey
Student ID: 71012029
Date: 5th August 2026
Role: Simple summary statistics for a list of numeric readings.

Complete the TODOs below.
"""


def mean(values):
    # TODO : if `values` is empty, raise ValueError("mean() needs values")
    # TODO : return the average (sum of values divided by how many there are)
    if len(values) == 0:
        raise ValueError("mean() needs values")
        return
    if not isinstance(values, str):
        try:
            avg = sum(values)/len(values)
        except TypeError:
            print('Invalid values')
    return avg

def minimum(values):
    # TODO: return the smallest value. Hint: the built-in min()
    if not isinstance(values, (list, tuple, set)):
        return
    try:
        minVal = min(values)
    except TypeError:
        print('Invalid data')
        return
    return minVal


def maximum(values):
    # TODO: return the largest value. Hint: the built-in max()
    if not isinstance(values, str):
        try:
            maxVal = max(values)
        except:
            print('Invalid values')
            return
    return maxVal


def spread(values):
    # TODO: return maximum(values) - minimum(values)
    sp = maximum(values) - minimum(values)
    return sp
