#!/usr/bin/python

# Project Euler
# Problem 55
# Lychrel numbers


import euler as eu


lychrel = 0
for x in range(1, 10001):
    iterations = 1
    rx = eu.reverse(x)
    while iterations <= 50:
        if iterations == 50:
            lychrel += 1
            break
        z = x + rx
        rz = eu.reverse(z)
        if z != rz:
            x, rx = z, rz
            iterations += 1
            continue
        else:
            print x, z, iterations
            iterations += 1
            break
print lychrel
