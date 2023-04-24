#!/usr/bin/python

# Project Euler
# Problem 47
# Distinct primes factors

from sympy import primefactors


def my_map(n):
    if len(primefactors(n)) == 4:
        return True
    else:
        return False


def all_true(my_set):
    for item in my_set:
        if not item:
            return False
    return True


for i in range(1, 1000000):
    working_set = [x for x in range(i, i+4)]
    check_set = [my_map(x) for x in working_set]
    if all_true(check_set):
        print(working_set)
        break
