"""Bootcamp Utility Module: A collection of statistical functions"""

# Import required functions
import numpy as np

# Emperical Cumulative Distrubution Function
def ecdf(data):
    """ Compute x, y values for an emperical distribution function"""

    # Sort our data
    x = np.sort(data)
    y = np.arange(1, 1 + len(x)) / len(x)

    return x, y
