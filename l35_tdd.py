import pytest
import bioinfo_dicts

def n_neg(seq):
    """computes the number of negative residues in a protein sequence"""

    #convert to upper case
    seq = seq.upper()

    #check for sequence validity
    for aa in seq:
        if aa not in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid')

    #count E's and D's, then return a count
    return seq.count('D') + seq.count('E')
