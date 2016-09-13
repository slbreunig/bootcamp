import numpy as np

xa_high = np.loadtxt('data/xa_high_food.csv', comments = '#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments = '#')

def xa_to_diameter(xa):
    """
    Convert an array of cross-sectional areas
    to dimeters with commensurate units
    """

    #compute diameter from areas
    #A = pi * d^2 / 4
    diameter = np.sqrt(xa * 4 / np.pi)

    return diameter
