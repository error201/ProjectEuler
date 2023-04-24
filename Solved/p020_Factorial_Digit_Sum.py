#!/usr/bin/python

import euler

sum = 0
for number in list(str(euler.factorial(100))):
    sum += int(number)
print sum