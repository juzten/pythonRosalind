#-----------------------------------------------------------------------------
# Name:  Justin Spain
# Email: juzten@gmail.com
# Date:
# File:  003_revc.py
#-----------------------------------------------------------------------------
# Edit log
# 11/17/2013 edit log here
#
#-----------------------------------------------------------------------------
# [TODO]
# todo list here
#
#-----------------------------------------------------------------------------


# Rosalind bioinformatics exercises
# Exersie: Complementing a Strand of DNA
# URL:     http://rosalind.info/problems/revc/


# Problem:
# In DNA strings, symbols 'A' and 'T' are complements of each other, as
# are 'C' and 'G'.
# The reverse complement of a DNA string s is the string sc formed by
# reversing the symbols of s, then taking the complement of each symbol
# (e.g., the reverse complement of "GTCA" is "TGAC").
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.
# Sample Dataset
# AAAACCCGGT
# Sample Output
# ACCGGGTTTT
# --notes
# GTCA
# ACTG = reverse
# TGAC = reverse complement
#-----------------------------------------------------------------------------
# Place any necessary functions below this.
#-----------------------------------------------------------------------------
def reverse_DNA(s):
    reverse = s[::-1]
    return reverse


def complement_DNA(reverse):
    complement = list(reverse)
    for index, val in enumerate(complement):
        if complement[index] == 'A':
            complement[index] = 'T'
        elif complement[index] == 'T':
            complement[index] = 'A'
        elif complement[index] == 'G':
            complement[index] = 'C'
        elif complement[index] == 'C':
            complement[index] = 'G'
    return ''.join(complement)

#-----------------------------------------------------------------------------
# Begin the main program.
#-----------------------------------------------------------------------------
# initialize variables
# DNA string
s = 'AAAACCCGGT'
# s = 'CGCTCTACTCCTGATATCCTAAAATGAGTAATCGAAATATTGCAGCAATCTGACCTGCGTGATTCGCATTCCACGAGTTGAGGTTTAAAACGGCTCTCCGGCCTATGGCTAATGTAGCAGGCAAGGAATCAACAGCGATAGATCCCGAGAAATGGTACATCTTGCGCTCGCGCGCGCACAAGCCAATCCCGGCGGACACAGCAGGATCCCAGCTGTTTTAAACAATAACAGGTAGCCGCACTCCGACCTATTCGTCATGGCGGCGAACAGACAACGCAGTTAGATTCGCTCGCCGTTACACGGGTCGGTAGACTCCCAGAACAGAAATCCTCGATTACCATAACATAATCCCTAAATCGATGTAGAAGTTGTGGTTGAATTTCGGTCGAGTTATGCAAACCACGGTGTACACCGAGACGTGCTCAATGAAGTCAGTGTAAACGTAGCCTTTCATGGTCCCTAGGTCTATGGGCCAGTTAGTCATTGCACCGACTTTCACAGGTAATTCCATATGGGTAAATATTTCGTGACCCAGTGTCCCTGTCCACATGAATGTGTCATTGGGTAGCATAGGTCCTACGAAAATTTACTTGCGTAGTCATCTCAATCATGATATAAGATTCGTCCACTCTTATATACTCCTGCGGACACAGAATGGGAAAATCGTCTCACAGGTGTCATCGGCCCGTCAACACGTGATAGCGACCCTCCAGCCTAGATATAAATAGTACTGCTAGAGCTGGGCGTATAAGGGTCTAACGGGGCAGTCTAATGGTATCAGACAGAGATCTCAAAGTGGGCTTATGAGTCTCGGCAGATCGGATACTGACAAGATCTTTGGAATAATATGCGCCGTCGCGCCGCCAATGATAGAACGTCCTAGTAGCCGTATTGATAATCATCTTATGTTGAGTATATTCCTTGAGATTCTACTCGATGAGCC'
# reverse of string
reverse = ''
# complement of string
complement = ''

reverse = reverse_DNA(s)
complement = complement_DNA(reverse)
print complement



# test
# py.test 003_revc.py
def test_reverse():
    s = 'AAAACCCGGT'
    assert reverse_DNA(s) == 'TGGCCCAAAA'

def test_complement_of_reverse():
    test_reverse = 'TGGCCCAAAA'
    assert complement_DNA(test_reverse) == 'ACCGGGTTTT'
