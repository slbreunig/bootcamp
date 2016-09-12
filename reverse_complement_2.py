
def rev_comp(sequence):
    reversed_sequence = sequence[::-1]
    reversed_sequence = reversed_sequence.lower()
    reversed_sequence = reversed_sequence.replace('a', 'T')
    reversed_sequence = reversed_sequence.replace('t', 'A')
    reversed_sequence = reversed_sequence.replace('g', 'C')
    reversed_sequence = reversed_sequence.replace('c', 'G')
    return reversed_sequence
