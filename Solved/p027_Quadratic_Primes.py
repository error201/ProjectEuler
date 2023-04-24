#!/usr/bin/python

# Project Euler
# Problem 27
# Quadratic primes


import euler as eu

highest = 0

def quad(a1, n1, b1):
    result = (n1*n1) + (a1*n1) + b1
    if eu.primality(result):
        return True
    else:
        return False

for b in xrange(-1000, 1001):
    for a in xrange(-1000, 1001):
        n = 0
        count = 0
        while quad(a, n, b):
            n += 1
            count += 1
        if count >= highest:
            highest = count
            print "%s, %s, %s : %s : %s" % (str(a), str(b), str(n), str(a * b), count)
