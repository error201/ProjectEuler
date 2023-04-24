#!/usr/bin/python


# Project Euler
# Problem 70
# Totient Permutation


from sympy import totient
from euler import single_perm


if __name__ == '__main__':
    my_min = 1000.0
    for n in range(6018162, 10000000):
        phi = totient(n)  
        if single_perm(n, phi):
            res = n/phi
            if res < my_min:
                my_min = res
                print('n: {0:>9,}, phi: {1:>9,}, res: {2:<12.10}'.format(n, phi, res))    
