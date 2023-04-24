#!/usr/bin/python

i = 1
my_sum = 0
primes = []


def is_prime(n: int) -> bool:
    """check if integer n is a prime"""
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
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


while i < 2000000:
    prime = is_prime(i)
    if prime == 1:
        primes.append(i)
    i += 1

for item in primes:
    my_sum += int(item)
print(my_sum)
