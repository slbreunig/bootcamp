def gc_blocks(seq, block_size):
    """Divides a given sequence into blocks of given size.
    For each, block, the GC content is computed and returned in a tuple."""

    #make the sequence all upper case
    seq = seq.upper()

    #initialize count variables
    index = 0
    count = 0

    #initialize block and gc_list
    block = ''
    gc_list = []

    #run entire length of sequence
    while index < len(seq) and len(seq[index:]) >= block_size:

        #determine each block and gc content
        while count < block_size:
            block += seq[index]
            count += 1
            index += 1

        #compute gc content from each block
        gc_number = block.count('C') + block.count('G')
        gc_fraction = gc_number / block_size
        gc_list += [gc_fraction]

        #reset count and block
        count = 0
        block = ''

    #convert gc_list to a tuple
    gc_tuple = tuple(gc_list)

    return gc_tuple

def gc_map(seq, block_size, gc_thresh):
    """Takes as an imput a sequence, block size, and set GC threshold.
    Returns the original sequence.
    Blocks with GC content > threshold are capitalized.
    Blocks with GC content < threshold are lowercase.
    Bases not included in blocks are truncated."""

    #initialize variables
    formatted_seq = ''

    while len(seq) >= block_size:

        #cut block
        block = seq[:block_size]

        #format block based on gc threshold
        if gc_blocks(block, block_size)[0] < gc_thresh:
            block = block.lower()

        #add block to working output sequence
        formatted_seq += block

        #remove block from seq
        seq = seq[block_size:]

    return formatted_seq
