#-----------------------------------------------------------------------------
# Name:  Justin Spain
# Email: juzten@gmail.com
# Date:  11/17/2013
# File:  002_rna.py
#-----------------------------------------------------------------------------
# Edit log
# 11/17/2013 created file
# 
#-----------------------------------------------------------------------------
# [TODO]
# 
# 
#-----------------------------------------------------------------------------


# Rosalind bioinformatics exercises
# Exersie: Transcribing DNA into RNA
# URL:     http://rosalind.info/problems/rna/


# Problem:

# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is 
# formed by replacing all occurrences of 'T' in t with 'U' in u.

# Given: A DNA string t having length at most 1000 nt.

# Return: The transcribed RNA string of t.

# Sample Dataset
# GATGGAACTTGACTACGTAAATT

# Sample Output
# GAUGGAACUUGACUACGUAAAUU



# --notes
# rna string = a, c, g, u
# dna string = a, c, g, t

#-----------------------------------------------------------------------------
# Place any necessary functions below this.
#-----------------------------------------------------------------------------
def convert_to_rna(t):
    # Place any line processing code here.
    # sets u contents to t contents
    # preserves original t
    u = t
    # replace any occurence of T with U
    u = u.replace('T', 'U')

    return u


#-----------------------------------------------------------------------------
# Begin the main program.
#-----------------------------------------------------------------------------
# initialize variables
# dna string
t = 'GATGGAACTTGACTACGTAAATT'
# t = 'CTAAGTAGGGTTCGGGCAATCGTATAGCTATGTTTATTACTTGATGAGATTCTGAGCTGGCCTCAGTACGCCTACTCCCAGTTTTCCCCCAGTGCTATCTCCCGGACCTAAAAGTCTTCTAGAATTCAGATTTATTTGCCAAGTCGCTTAACGGGCGTGGCCCGGACTATTGGGGCGTACTCTAAACGTGCGGAGTTAACTCATTGGTCGGGTTGATACGCCGACCGGGCACCGCCAACTTTTATGCGGGAACTCAAACTAATTCCCTGTTTACCAGTAGGACGGGCTGTTGCCCACTGGGCCGCGCGCTTAGCCAGCGTTTGCGGACCCCGAATGGACCGGGTACCATGCGTAATTCCAATGTCGGGCTGAATTCTAGTTAAGTCCTATTAGAGAGGTTTACATAGTCCAGTTAAATGGCCCACGGGTTCTATCACTTCCTGGCAGCGATCCGATTCAACTGGCGGGATATGGCGACCGGTGCCAGCTGGGTCTTTTGAGTCCCACGCAGAATACCGAAATACCGTAGTTTACTATAACCCTGAGTAGCGTTAAGGGCACCAGCACGCAGCGCAAAAGCTGCCATTAATCAGCAAGAGAGACAAGGTACAGTTGCCGCCTTGTCCATGATAATACGGCATGGCTCGCTCATCGCACGGCACGCCGAAAATCAGACTCCAAGAGAGGTACAATAGCCGTTACCAAAACTACTGCATAATAGTGTTCTTGGCCGTAAGTAACGAATAATATGGTGAATGACTGAACTTCAAGTGTTCGGCCTTTGCCTCGTGACACTGCAAGTACGACAAATCGAACTAGTTAACGGCCCATCGGCCGGTCCGCATGGAAGCGATAGCTCCCGGCTAGGCTCCCCGCTTTTGATCGACACACGAGCGTGTGTGCTGGGAGAATGGAATTACCCATATAGTTGCGCGCCGTGCAGAGTGGCTCGCT'
# u will be rna string
u = convert_to_rna(t)
# prints original dna string
print t
# prints new rna string
print u


# test
# py.test 002_rna.py
def test_one():
	t = 'GATGGAACTTGACTACGTAAATT'
	assert convert_to_rna(t) == 'GAUGGAACUUGACUACGUAAAUU'
def test_two():
	d = 'CTAAGTAGGGTTCGGGCAATCGTATAGCTATGTTTATTACTTGATGAGATTCTGAGCTGGCCTCAGTACGCCTACTCCCAGTTTTCCCCCAGTGCTATCTCCCGGACCTAAAAGTCTTCTAGAATTCAGATTTATTTGCCAAGTCGCTTAACGGGCGTGGCCCGGACTATTGGGGCGTACTCTAAACGTGCGGAGTTAACTCATTGGTCGGGTTGATACGCCGACCGGGCACCGCCAACTTTTATGCGGGAACTCAAACTAATTCCCTGTTTACCAGTAGGACGGGCTGTTGCCCACTGGGCCGCGCGCTTAGCCAGCGTTTGCGGACCCCGAATGGACCGGGTACCATGCGTAATTCCAATGTCGGGCTGAATTCTAGTTAAGTCCTATTAGAGAGGTTTACATAGTCCAGTTAAATGGCCCACGGGTTCTATCACTTCCTGGCAGCGATCCGATTCAACTGGCGGGATATGGCGACCGGTGCCAGCTGGGTCTTTTGAGTCCCACGCAGAATACCGAAATACCGTAGTTTACTATAACCCTGAGTAGCGTTAAGGGCACCAGCACGCAGCGCAAAAGCTGCCATTAATCAGCAAGAGAGACAAGGTACAGTTGCCGCCTTGTCCATGATAATACGGCATGGCTCGCTCATCGCACGGCACGCCGAAAATCAGACTCCAAGAGAGGTACAATAGCCGTTACCAAAACTACTGCATAATAGTGTTCTTGGCCGTAAGTAACGAATAATATGGTGAATGACTGAACTTCAAGTGTTCGGCCTTTGCCTCGTGACACTGCAAGTACGACAAATCGAACTAGTTAACGGCCCATCGGCCGGTCCGCATGGAAGCGATAGCTCCCGGCTAGGCTCCCCGCTTTTGATCGACACACGAGCGTGTGTGCTGGGAGAATGGAATTACCCATATAGTTGCGCGCCGTGCAGAGTGGCTCGCT'
	assert convert_to_rna(d) == 'CUAAGUAGGGUUCGGGCAAUCGUAUAGCUAUGUUUAUUACUUGAUGAGAUUCUGAGCUGGCCUCAGUACGCCUACUCCCAGUUUUCCCCCAGUGCUAUCUCCCGGACCUAAAAGUCUUCUAGAAUUCAGAUUUAUUUGCCAAGUCGCUUAACGGGCGUGGCCCGGACUAUUGGGGCGUACUCUAAACGUGCGGAGUUAACUCAUUGGUCGGGUUGAUACGCCGACCGGGCACCGCCAACUUUUAUGCGGGAACUCAAACUAAUUCCCUGUUUACCAGUAGGACGGGCUGUUGCCCACUGGGCCGCGCGCUUAGCCAGCGUUUGCGGACCCCGAAUGGACCGGGUACCAUGCGUAAUUCCAAUGUCGGGCUGAAUUCUAGUUAAGUCCUAUUAGAGAGGUUUACAUAGUCCAGUUAAAUGGCCCACGGGUUCUAUCACUUCCUGGCAGCGAUCCGAUUCAACUGGCGGGAUAUGGCGACCGGUGCCAGCUGGGUCUUUUGAGUCCCACGCAGAAUACCGAAAUACCGUAGUUUACUAUAACCCUGAGUAGCGUUAAGGGCACCAGCACGCAGCGCAAAAGCUGCCAUUAAUCAGCAAGAGAGACAAGGUACAGUUGCCGCCUUGUCCAUGAUAAUACGGCAUGGCUCGCUCAUCGCACGGCACGCCGAAAAUCAGACUCCAAGAGAGGUACAAUAGCCGUUACCAAAACUACUGCAUAAUAGUGUUCUUGGCCGUAAGUAACGAAUAAUAUGGUGAAUGACUGAACUUCAAGUGUUCGGCCUUUGCCUCGUGACACUGCAAGUACGACAAAUCGAACUAGUUAACGGCCCAUCGGCCGGUCCGCAUGGAAGCGAUAGCUCCCGGCUAGGCUCCCCGCUUUUGAUCGACACACGAGCGUGUGUGCUGGGAGAAUGGAAUUACCCAUAUAGUUGCGCGCCGUGCAGAGUGGCUCGCU'
