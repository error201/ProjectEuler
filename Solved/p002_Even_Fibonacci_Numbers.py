#!/usr/bin/python

a = 1
b = 1
limit = 4000000
my_sum = 0

while b <= limit:
    a = a + b
    a, b = b, a
    if a % 2 == 0:
        my_sum += a
print(my_sum)
