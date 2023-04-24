#!/usr/bin/python

# Project Euler
# Problem 51
# Prime Digit Replacements


from sympy import nextprime
from euler import is_prime


current_prime = 11
results = {}
while current_prime:
    for i in range(0, len(str(current_prime))):
        my_count = 1
        primes = [str(current_prime)]
        for k in range(0, len(str(current_prime))):
            test_prime = list(str(current_prime))
            for l in range(0, 10):
                test_prime[i] = str(l)
                test_prime[k] = str(l)
                this_prime = ''.join(test_prime)
                # print(this_prime)
                if is_prime(int(this_prime)):
                    if this_prime not in primes:
                        my_count += 1
                        primes.append(this_prime)
    results[current_prime] = primes
    print(f'{current_prime}: {my_count  }:  {primes}')
    if my_count == 8:
        break
    else:
        current_prime = nextprime(current_prime)
