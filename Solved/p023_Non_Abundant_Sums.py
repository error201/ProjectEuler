#!/usr/bin/python

# Project Euler Problem 23
# Non-abundant sums

import euler as eu
import collections as coll

def number_type(n):
    my_sum = 0
    factor_list = eu.list_factors(n)[:-1]
    for my_number in factor_list:
        my_sum += int(my_number)
    # print str(n) + " : ", factor_list, " : ", my_sum
    # Perfect number:
    if my_sum == n:
        return 0
    # Abundant number:
    elif my_sum > n:
        return 1
    # Deficient number:
    else:
        return -1

if __name__ == '__main__':
    abundants = []
    abundant_sums = []
    filtered_sums = []
    my_numbers = []
    final_value = 0
    for x in xrange(1, 28124):
        if number_type(x) == 1:
            abundants.append(x)
    [abundant_sums.append(x + y) for x in abundants for y in abundants]
    [filtered_sums.append(x) for x in abundant_sums if x < 28124]
    c = coll.Counter(filtered_sums)
    final_sums = list(c)
    [my_numbers.append(x) for x in xrange(1,28124) if x not in final_sums]
    for item in my_numbers:
        final_value += item
    print final_value