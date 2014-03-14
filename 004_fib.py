#-----------------------------------------------------------------------------
# Name:  Justin Spain
# Email: juzten@gmail.com
# Date:
# File:  004_fib.py
#-----------------------------------------------------------------------------
# Edit log
# 03/14/2014 completed rosalind test
#
#-----------------------------------------------------------------------------
# [TODO]
# todo list here
#
#-----------------------------------------------------------------------------


# Rosalind bioinformatics exercises
# Exersie: Rabbits and Recurrence Relations
# URL:     http://rosalind.info/problems/fib/



# Problem:

# When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n. This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

# Given: Positive integers n<=40 and k<=5.

# Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# Sample Dataset
# 5 3
# Sample Output
# 19

# tested data
# totalMonths = 34
# offspringPerPair = 5
# answer is 313507166394911

#-----------------------------------------------------------------------------
# --notes
# A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior

# m1
# 1

# m2
# 1

# m3
# 1(3)

# m4
# 1(3)(3)

# m5
# 1(3.9)(3)(3)

# newBorns = 1
# newPregnant = 0
# adults = 0

# after 2 month
# newBorns = 0
# newPregnant = 1
# adults = 0

# after 3 months
# newBorns = 3
# newPregnant = 0
# adults = 1

# after 4 months
# newBorns = 3
# newPregnant = 3
# adults = 1

# after 5 months
# newBorns = 12
# newPregnant = 3
# adults = 4

# after 6 months
# newBorns = 21
# newPregnant = 12
# adults = 7



# first month
# 1, 0, 0
# second month
# 0, 1, 0
# 3rd month
# adults += newPregnant
# newPregnant = newBorns
# newBorns = adults * 3
# 4th month

#-----------------------------------------------------------------------------
# Place any necessary functions below this.
#-----------------------------------------------------------------------------
def loopThruMonths(totalMonths , offspringPerPair):
    month = 1
    newBorns = 1
    newPregnant = 0
    adults = 0
    total = 0

    if month == 1 and totalMonths >=1:
        newBorns = 1
        newPregnant = 0
        adults = 0
        month += 1
    if month == 2 and totalMonths >=2:
        newBorns = 0
        newPregnant = 1
        adults = 0
        month += 1

    while month > 2 and month <= totalMonths:
        adults += newPregnant
        newPregnant = newBorns
        newBorns = adults * offspringPerPair
        total = adults + newPregnant + newBorns
        month +=1
    varList = [newBorns, newPregnant, adults, total]

    return varList


#-----------------------------------------------------------------------------
# Begin the main program.
#-----------------------------------------------------------------------------
# initialize variables

totalMonths = 5
offspringPerPair = 3


if totalMonths <= 40 and offspringPerPair <= 5:
    newBorns, newPregnant, adults, total = loopThruMonths(totalMonths, offspringPerPair)
    print 'adults: ' , adults
    print 'newPregnant: ' , newPregnant
    print 'newBorns: ' , newBorns
    print 'total: ' , total
else:
    print 'Total months has to be 40 or below and total \n offspring per rabbit pair has to be 5 or below!'



#-----------------------------------------------------------------------------
# test
#-----------------------------------------------------------------------------

# py.test 004_fib.py
def test_one():
    totalMonths = 5
    offspringPerPair = 3
    newBorns, newPregnant, adults, total = loopThruMonths(totalMonths, offspringPerPair)
    assert  total == 19

def test_two():
    totalMonths = 34
    offspringPerPair = 5
    newBorns, newPregnant, adults, total = loopThruMonths(totalMonths, offspringPerPair)
    assert  total == 313507166394911
