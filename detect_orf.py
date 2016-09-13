def find_start(seq):
    """Finds all of the start codons within a given sequence
    and returns the index of the start of the codon"""

    #initialize
    start_spaces = []
    seq = seq.upper()
    index = 0

    while index < len(seq):
        if seq[index] == 'A' and seq[index + 1] == 'T' and seq[index + 2] == 'G':
            start_spaces.append(index)
        index += 1

    return start_spaces


def find_end(seq):
    """Finds all of the stop codons within a given sequence
    and returns the indices of these codons"""

    #validate
    if validate_seq(seq):

        #initialize
        stop_spaces = []
        seq = seq.upper()
        index = 0

        while index < len(seq):
            if (seq[index] == 'T' and seq[index + 1] == 'G' and seq[index + 2] == 'A')\
            or (seq[index] == 'T' and seq[index + 1] == 'A' and seq[index + 2] == 'G')\
            or (seq[index] == 'T' and seq[index + 1] == 'A' and seq[index + 2] == 'A'):
                stop_spaces.append(index)
            index += 1

        return stop_spaces

    #invalid base in sequence 
    else:
        print ('Invalid sequence')

def validate_seq(seq):
    """Ensures that all bases within a given sequence are valid"""

    valid_bases = ['G', 'A', 'T', 'C']
    valid = True

    for i in seq:
        if i not in valid_bases:
            valid = False

    return valid
