#!/usr/bin/python

sums = 0

for number in range(1, 1000):
    if number % 3 == 0 or number % 5 == 0:
        print(number)
        sums += number
print(sums)
