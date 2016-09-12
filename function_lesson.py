def ratio(x,y):
    """The ratio of x to y"""
    return x/y

def answer_life_universe_everything():
    '''simpler program'''
    return 42

def think_too_much():
    """express Caesar's skepticism about Cassius."""

    print("""Yond Cassius has a lean and hungry look,
    He thinks too much; such men are dangerous
    And should be avoided""")

def complement_base(base, material = 'DNA'):
    """Return the Watson-Crick complementary base"""
    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
        else:
            raise RuntimeError ('Invalid material')
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

def reverse_complement(seq, material = 'DNA'):
    """Compute reverse complement of a nucleic acid sequence"""

    #initialize empty string
    rev_comp = ''

    #loop through and add new rev comp bases
    for base in reversed(seq):
        rev_comp += complement_base(base, material = material)

    return rev_comp
