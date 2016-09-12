def complement_seq(seq):
    position = 0
    nseq = ''
    for base in seq:
        if base == 'A':
            nbase = 'T'
        elif base == 'T':
            nbase = 'A'
        elif base == 'G':
            nbase = 'C'
        elif base == 'C':
            nbase = 'G'
        else:
            print ('Position ', position + 1, ' is not a valid base letter')
        nseq += nbase
    return nseq

def reverse_complement(comp_seq):
    rev_seq = ''
    n = len(comp_seq)
    while n > 0:
        rev_seq += comp_seq[-1]
        comp_seq = comp_seq[0:-1]
        n -= 1
    return rev_seq

def find_rev_comp(sequence):
    return reverse_complement(complement_seq(sequence))
