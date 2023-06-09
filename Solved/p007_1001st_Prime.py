#!/usr/bin/python

i = 1
primes = []


def is_prime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the square root of n
    # for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return n


while i:
    value = is_prime(i)
    if value:
        primes.append(value)
        if len(primes) == 10001:
            print(value)
            for item in primes:
                print(item)
    i += 1
