import pytest
import l36_tddpractice as prac

sequence = 'ATGGAGAACAACGAAGCCCCCTCCCCCTCGGGATCCAACAACAA\
CGAGAACAACAATGCAGCCCAGAAGAAGCTGCAGCAGACCCAAGCCAAGGTGGACG\
AGGTGGTCGGGATTATGCGTGTGAACGTGGAGAAGGTCCTGGAGCGGGACCAGAAG\
CTATCGGAACTGGGCGAGCGTGCGGATCAGCTGGAGCAGGGAGCATCCCAGTTCGA\
GCAGCAGGCCGGCAAGCTGAAGCGCAAGCAATGGTGGGCCAACATGAAGATGATGA\
TCATTCTGGGCGTGATAGCCGTTGTGCTGCTCATCATCGTTCTGGTGTCGCTTTTC\
AATTGA'
seq_lower = sequence.lower()

def test_find_codon():

    assert prac.find_codon('ATG', sequence) == 0
    assert prac.find_codon('atg', sequence) == 0
    assert prac.find_codon('atg', seq_lower) == 0
    assert prac.find_codon('ATG', seq_lower) == 0
    assert prac.find_codon('AAT', sequence) == 54
    assert prac.find_codon('TGT', sequence) == -1
    assert prac.find_codon('TGC', sequence) == -1

    pytest.raises(RuntimeError, "prac.find_codon('ZWB')")

#***INCOMPLETE***
