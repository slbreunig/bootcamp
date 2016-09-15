"""Bootcamp Utility Module: A collection of statistical functions"""

# Import required functions
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Emperical Cumulative Distrubution Function
def ecdf(data):
    """ Compute x, y values for an emperical distribution function.
    Returns a tuple."""

    # Sort our data
    x = np.sort(data)
    y = np.arange(1, 1 + len(x)) / len(x)

    return x, y

# Bootstrap Replicates Generation Function
def draw_bs_reps(data, func, size=1):
    """ This function draws bootstrap replicates.
    data is an array, function is desired statistical calculation
    (eg np.mean, np.std, np.median, or user-defined etc)
    size is the number of replicates to be generated. """

    # length of data input
    n = len(data)
    # Array for number of replicates
    reps = np.empty(size)

    for i in range(size):
        # Draw a bootstrap sample
        bs_sample = np.random.choice(data, replace=True, size=n)
        # Apply desired function to bootstrap sample
        reps[i] = func(bs_sample)

    return reps

# Compute confidence interval
def conf_int(data, interval=95):
    """Computes the confidence interval for a given data set
    and returns the low and high values as an array"""

    low_range = (100-interval)/2
    high_range = low_range + interval
    confidence_interval = np.percentile(data, low_range, high_range)

    return confidence_interval
