#!/usr/bin/python

# Project Euler
# Problem 45
# Triangular, pentagonal, and hexagonal

import euler as eu

for x in xrange(1, 10000000):
    tri = eu.triangular(x)
    if eu.pentagonality(tri):
        if eu.hexagonality(tri):
            print tri
