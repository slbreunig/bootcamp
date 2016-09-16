

def find_codon(codon, seq):
    '''Find a specified codon within a given sequence'''
    #format incoming seqence and codon to allow for upper/lower
    codon = codon.upper()
    seq = seq.upper()

    print ('codon')
    print (seq)

    i = 0
    #scan sequence until we hit start codon, or end of sequence
    while seq[i:i+3] != codon and i< len(seq):
        i += 1

    if i == len(seq):
        return -1

    return i

#***INCOMPLETE***
