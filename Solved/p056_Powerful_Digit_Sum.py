#!/usr/bin/python

# Project Euler
# Problem 56
# Powerful digit my_sum


from functools import reduce

maximum = 0

for a in range(2, 100):
    for b in range(1, 100):
        digits = list(str(a**b))
        my_sum = reduce(lambda x, y: int(x)+int(y), digits)
        print("{0}^{1}: {2}".format(a, b, my_sum))
        if int(my_sum) > maximum:
            maximum = int(my_sum)

print(maximum)
