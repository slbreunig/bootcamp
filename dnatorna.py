""" convert DNA sequences to RNA """

def rna(seq):
    """ convert a DNA sequence to RNA, in all upper case"""

    #convert to uppercase
    seq = seq.upper()

    return seq.replace ('T', 'U')
