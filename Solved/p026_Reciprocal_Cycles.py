#!/usr/bin/python

# Project Euler
# Problem 80
# Square root digital expansion

import re
import decimal

repeating_pattern = re.compile(r'([0-9]+?)\1+?')


def find_repeating_digits(my_number):
    number_string = str(my_number)
    # if repeating_pattern.findall(number_string):
    my_match = repeating_pattern.findall(number_string)
    if my_match:
        longest = 0
        for index, item in enumerate(my_match):
            if len(item) > longest:
                longest = index
        return my_match[longest], len(my_match[longest])
    else:
        return None

if __name__ == "__main__":
    decimal.getcontext().prec = 2000
    longest = 0
    for x in xrange(1, 1001):
        current_number = decimal.Decimal(1)/decimal.Decimal(x)
        my_digits = find_repeating_digits(current_number)
        if my_digits:
            if my_digits[1] > longest:
                longest = my_digits[1]
                print x, ":", my_digits[1]