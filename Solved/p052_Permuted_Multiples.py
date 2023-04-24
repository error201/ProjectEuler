#!/usr/bin/python

# Project Euler
# Problem 52
# Permuted multiples


import euler as eu
import sys

for n in xrange(1, 1000000):
    results = eu.perms(n)
    if len(results) >= 6:
        for item in results:
            if str(2*int(item)) in results:
                if str(3*int(item)) in results:
                    if str(4*int(item)) in results:
                        if str(5*int(item)) in results:
                            if str(6*int(item)) in results:
                                print item
                                sys.exit()
