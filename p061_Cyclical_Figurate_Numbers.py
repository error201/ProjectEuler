#!/usr/bin/python


# Project Euler
# Problem 61
# Cyclical figurate numbers


import euler as eu


pool = []
three_set = set(eu.triangular_series(4))
four_set = set(eu.square_series(4))
five_set = set(eu.pentagonal_series(4))
six_set = set(eu.hexagonal_series(4))
seven_set = set(eu.heptagonal_series(4))
eight_set = set(eu.octagonal_series(4))

sets = [three_set, four_set, five_set, six_set, seven_set, eight_set]

for i in sets:
    for j in sets:
        if j == i:
            continue
        else:
            for item in i.intersection(j):
                pool.append(item)
print(len(pool))
