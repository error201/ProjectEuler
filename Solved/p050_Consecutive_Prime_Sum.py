#!/usr/bin/python

# Project Euler
# Problem 50
# Consecutive prime my_sum


import euler as eu

primes = eu.prime_list(1, 1000000)
current = 0
last = len(primes)
end = 0
highest = 0
total = 0
count = 0

while current <= last:
    end = current
    while end <= last:
        total = 0
        for x in primes[current:end]:
            total += x
        if total > 1000000:
            break
        count = end - current
        if eu.primality(total):
            if count > highest:
                highest = count
                print current, end, count, total
        end += 1
    current += 1

