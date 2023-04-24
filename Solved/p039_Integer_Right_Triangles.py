#!/usr/bin/python

# Project Euler
# Problem 39
# Integer Right Triangles


import math


maximum = 0
solutions = {}
for p in range(1, 1001):
    for a in range(1, 1001):
        for b in range(a, 1001):
            c = math.sqrt((a*a)+(b*b))
            if c.is_integer():
                x = a + b + c
                if x == p:
                    if p in solutions:
                        solutions[p] += 1
                    else:
                        solutions[p] = 1
for perimeter, num_solutions in solutions.items():
    if num_solutions > maximum:
        maximum = num_solutions
        print("%d:    %d" % (perimeter, num_solutions))
