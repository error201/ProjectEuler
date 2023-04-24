#!/usr/bin/python

# Project Euler
# Problem 44
# Pentagon numbers

import euler as eu

results = {}
for x in xrange(1, 10000):
    p_j = eu.pentagonal(x)
    for y in xrange(1, 10000):
        terms = []
        p_k = eu.pentagonal(y)
        pent_sum = p_j + p_k
        if eu.pentagonality(pent_sum):
            D = abs(p_k - p_j)
            if eu.pentagonality(D):
                terms.append(p_j)
                terms.append(p_k)
                results[D] = terms
print results
