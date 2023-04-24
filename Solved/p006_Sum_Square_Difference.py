#!/usr/bin/python

sums = sum([x ** 2 for x in range(1, 101)])
print(sums)
product = (sum([x for x in range(1, 101)])) ** 2
print(product)
print(product - sums)
