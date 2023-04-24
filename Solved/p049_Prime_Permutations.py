#!/usr/bin/python

# Project Euler
# Problem 49
# Prime Permutations


import euler as eu
import itertools

four_primes = []

for x in xrange(999, 10000):
    if eu.primality(x):
        four_primes.append(x)

for x in four_primes:
    my_perms = []
    temp_x = list(str(x))
    perms = itertools.permutations(temp_x, 4)
    for item in perms:
        temp_string = ''.join(item)
        int_string = int(temp_string)
        if eu.primality(int_string):
            if int_string >= 1000:
                if int_string not in my_perms:
                    my_perms.append(int_string)
    if len(my_perms) >= 3:
        my_perms.sort()
        for item1 in my_perms:
            for item2 in my_perms:
                difference = abs(item1-item2)
                new_num = item2 + difference
                if new_num in my_perms:
                    if new_num != item1:
                        print item1, item2, new_num
                        break