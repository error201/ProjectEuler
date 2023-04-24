#!/usr/bin/python

# Project Euler
# Problem 40
# Champernowne's Constant

import euler as eu

place = 0
product = 1
for x in xrange(1, 1000000):
    num_string = str(x)
    for y in num_string:
        place += 1
        if place == 1:
            print "d1 : ", y
            product *= int(y)
        elif place == 10:
            print "d10 : ", y
            product *= int(y)
        elif place == 100:
            print "d100 : ", y
            product *= int(y)
        elif place == 1000:
            print "d1000 : ", y
            product *= int(y)
        elif place == 10000:
            print "d10000 : ", y
            product *= int(y)
        elif place == 100000:
            print "d100000 : ", y
            product *= int(y)
        elif place == 1000000:
            print "d1000000 : ", y
            product *= int(y)
print product