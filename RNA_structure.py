#def RNA_structure_validator(RNA, structure):
    #"""This program determines if the entered structure for a given
    #RNA sequence is a valid configuration"""

#This program is not complete

def validate_par(structure):
    """This function validates the number of open and closed parenthases"""
    open_par = structure.count('(')
    closed_par = structure.count(')')
    return open_par == closed_par

def dotparen_to_bp(structure):
    """This function converts the input structure to tuple, base pair notation"""
    #initialize
    bp_tuple = tuple()

    #initialize variables for period and parenthases list constructions
    #parenthases
    structure_list = list(structure)
    par_positions = []
    i = 0
    #period
    structure_list_2 = structure_list
    period_positions = []
    j = 0

    #makes a list of all of the indices of the parenthases
    while len(structure_list) != 0:
        character = structure_list.pop(0)
        if character in "()":
            par_positions.append(i)
        i += 1

    #makes a list of the period indices
    while len(structure-list_2) != 0:
        character = structure_list_2.pop(0)
        if character = '.':
            period_positions.append(j)
        j += 1

    return par_positions
