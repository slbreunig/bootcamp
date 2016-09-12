def find_longest_sub(string_1, string_2):
    #initialize
    longest_length = 0
    longest_sequence = ''

    #definie shortest and longest strings
    if len(string_1) > len(string_2):
        short_string = string_2
        long_string = string_1
    else:
        short_string = string_1
        long_string = string_2

    m = 1
    n = 1
    for i in short_string:

        #initialize
        current_sequence = i
        n = m

        while current_sequence in long_string and n < len(short_string):
            current_sequence += short_string[n]
            n += 1

        if len(current_sequence) > longest_length:
            longest_sequence = current_sequence
            longest_length = len(longest_sequence)

        m += 1

    return longest_sequence
