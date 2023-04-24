#!/usr/bin/python

# Project Euler
# Problem 66
# Diophantine equation


from sympy.solvers.diophantine import diop_DN

max_x = 0
max_d = 0
max_y = 0
for D in range(2, 1001):
    x, y = diop_DN(D, 1)[0]
    if x > max_x:
        max_x = x
        max_d = D
        max_y = y
print('D: {2}, x:{0}, y:{1}'.format(max_x, max_y, max_d))
