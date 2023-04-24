#!/usr/bin/python

# Project Euler
# Problem 30
# Digit Fifth Powers

# import euler as eu

for x in xrange(2, 99999):
    total = 0
    num_str = str(x)
    for digit in num_str:
        total += int(digit)**5
    if total == x:
        print x, " : ", total