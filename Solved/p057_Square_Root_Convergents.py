#!/usr/bin/python

# Project Euler
# Problem 57
# Square Root Convergents


from __future__ import division
from sympy import *


def list_to_frac(l):
    expr = Integer(0)
    for i in reversed(l[1:]):
        expr += i
        expr = 1 / expr
    return fraction(l[0] + expr)


def count_digits(n):
    my_string = str(n)
    return len(my_string)


if __name__ == "__main__":
    a = [1, 2]
    my_count = 0

    while len(a) - 1 <= 1000:
        my_fraction = list_to_frac(a)
        length_numer = count_digits(my_fraction[0])
        length_denom = count_digits(my_fraction[1])
        if length_numer > length_denom:
            my_count += 1
        a.append(2)
    print(my_count)