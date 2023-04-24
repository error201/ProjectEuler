#!/usr/bin/python

# Project Euler
# Problem 41
# Pandigital prime


import sys
import euler as eu


for number in xrange(2, 987654321):
    if eu.is_prime(number):
        if eu.is_pandigital(number):
            print number
