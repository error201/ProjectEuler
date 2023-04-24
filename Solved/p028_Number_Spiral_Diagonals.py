#!/usr/bin/python

# Project Euler
# Problem 80
# Number Spiral Diagonals

if __name__ == "__main__":
    my_sum = 1
    for x in xrange(1, 501):
        row = ((x*2)+1)
        if row <= 1001:
            ur = (((x*2)+1)**2)
            br = (((x*2)+1)**2)-(2*x)
            bl = (((x*2)+1)**2)-(4*x)
            ul = (((x*2)+1)**2)-(6*x)
            total = ur + br + bl + ul
            my_sum += total
            print x, ":", row, ":", total, ":", my_sum