#!/usr/bin/python

# Project Euler
# Problem 53
# Combinatoric selections


import math


def nCr(n, r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n - r))

amount = 0
for i in range(2, 101):
    for j in range(1, i+1):
        result = nCr(i, j)
        if result > 1000000:
            amount += 1
print amount