#!/usr/bin/python

# Project Euler
# Problem 78
# Coin partitions


from sympy.utilities.iterables import partitions


for n in range(1, 100):
    my_count = 0
    num_parts = partitions(n)
    my_count = sum(1 for _ in num_parts)
    if my_count % 1000000 == 0:
        print(n)
