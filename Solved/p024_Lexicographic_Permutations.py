#!/usr/bin/python

# Project Euler
# Problem 24 - Lexicographic permutations

from itertools import permutations

pool = '0123456789'
choose = 10

for index, item in enumerate(permutations(pool, choose)):
    true_index = index + 1
    if true_index == 1000000:
        print item
