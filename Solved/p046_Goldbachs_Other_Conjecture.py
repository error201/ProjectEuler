#!/usr/bin/python

# Project Euler
# Problem 46
# Goldbach's other conjecture


import math
import euler as eu

things = []
limit = 10000
for i in xrange(3, limit+1, 2):
    if not eu.primality(i):
        things.append(i)
        for j in range(1, i):
            if eu.primality(j):
                k = math.sqrt((i-j)/2)
                if k.is_integer():
                    print "%d = %d + 2 x (%d)(%d)" % (i, j, k, k)
                    things.remove(i)
                    break
    else:
        print "%d is prime" % i
print '\n\n'
print things
