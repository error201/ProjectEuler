#!/usr/bin/python

# Project Euler
# Problem 35
# Circular Primes

import euler as eu
from collections import deque


def rotate_digits(n):
    digit_collection = []
    digit_stack = deque(str(n))
    number_len = len(digit_stack)-2
    digit_collection.append(int(n))
    while number_len >= 0:
        digit_stack.rotate()
        new_num = ""
        for digit in digit_stack:
            new_num += digit
        digit_collection.append(int(new_num))
        number_len -= 1
    return digit_collection

if __name__ == "__main__":
    count = 0
    for current_num in xrange(1, 1000001):
        primes = []
        variations = set(rotate_digits(current_num))
        for variant in variations:
            if eu.primality(variant):
                primes.append(variant)
        prime_set = set(primes)
        if not variations - prime_set:
            print current_num
            count += 1
    print count