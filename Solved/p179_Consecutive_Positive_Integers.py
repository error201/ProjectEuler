#!/usr/bin/python

# Project Euler
# Problem 179
# Consecutive Positive Integers


from sympy import divisor_count


my_count = 0
current = 0
previous = 0


for n in range(2, (10**7)+1):
    current = divisor_count(n)
    if current == previous:
        my_count += 1
        print('{:>9}, {:>9} have the same number of divisors.'.format(n-1, n))
    previous = current

print(my_count)
