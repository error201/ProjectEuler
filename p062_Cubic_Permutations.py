#!/usr/bin/python
import sys

# Project Euler
# Problem 62
# Cubic permutations


from euler import cube_root
from itertools import permutations


def is_cube(n):
    if cube_root(int(n)):
        return True
    else:
        return False


def perms(number) -> list:
    stuff = []
    my_length = len(number)
    for item in permutations(number, my_length):
        other_stuff = ''
        for element in item:
            other_stuff += element
            if len(other_stuff) == my_length:
                if int(other_stuff) not in stuff:
                    stuff.append(int(other_stuff))
    return [x for x in stuff if len(str(x)) == my_length]


for i in range(345, 5000):
    cubed = pow(int(i), 3)
    working_list = perms(str(cubed))
    check_set = [is_cube(x) for x in working_list]
    my_count = check_set.count(True)
    if my_count > 2 :
        if my_count >= 5:
            print(f'{i}, {cubed}: {my_count}')
            sys.exit()
        else:
            print(f'{i}, {cubed}: {my_count}')
