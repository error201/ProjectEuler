#!/usr/bin/python

# Project Euler
# Problem 35
# Circular Primes

from fractions import Fraction


if __name__ == "__main__":
    fraction_list: list = []
    for d in range(1, 1000001):
        for n in range(1, d):
            my_fraction = Fraction(n, d)
            if my_fraction not in fraction_list:
                # print(my_fraction)
                fraction_list.append(my_fraction)
    # fraction_list.sort()
    print(len(fraction_list))
