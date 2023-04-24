#!/usr/bin/python

# Project Euler
# Problem 85
# Counting rectangles


import math


def n_choose_r(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


size = (0, 0, 0, 0, 2000000)
for i in range(2, 500):
    for j in range(2, 500):
        rectangles = (n_choose_r(i + 1, 2) * n_choose_r(j + 1, 2))
        area = i * j
        target = 2000000
        difference = abs(target - rectangles)
        if difference < size[4]:
            size = (i, j, rectangles, area, difference)
print(size)
