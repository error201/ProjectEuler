#!/usr/bin/python

# Project Euler
# Problem 31
# Coin Sums

import euler as eu

total = 0
for x in xrange(2, 10000000):
    my_sum = 0
    num_str = str(x)
    for digit in num_str:
        my_sum += eu.factorial(int(digit))
    if my_sum == x:
        total += my_sum
        print x, " : ", my_sum
print total