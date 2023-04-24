#!/usr/bin/python

# Project Euler
# Problem 21 - Amicable Numbers


import euler as eu


def amicable(a):
    b = 0
    a_divisor_sum = 0
    b_divisor_sum = 0
    
    a_divisors = eu.factors(a)[:-1]
    for term in a_divisors:
        a_divisor_sum += term
#        print a_divisor_sum
    b = a_divisor_sum
    
    b_divisors = eu.factors(b)[:-1]
    for term in b_divisors:
        b_divisor_sum += term
#        print b_divisor_sum
    if a != b:
        if b_divisor_sum == a:
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    total = 0
    for number in range(2, 10000):
        if amicable(number):
            total += number
    print(total)
