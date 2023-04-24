#!/usr/bin/python


# Project Euler
# Problem 69
# Totient Maximum


from sympy import totient


if __name__ == '__main__':
    my_max = 0.0
    for n in range(1, 1000000):
        phi = totient(n)
        res = n/phi
        if res > my_max:
            my_max = res
            print('phi: {0}, n: {1}, phi/n: {2}'.format(phi, n, res))
