#!/usr/bin/python

# Project Euler
# Problem 37
# Truncatable Primes

import euler as eu
import collections


def truncatable(n):
    from_left = 1
    from_right = 1
    left_deque = collections.deque(str(n))
    right_deque = collections.deque(str(n))
    while left_deque:
        my_l_num = ''
        # print left_deque
        for element in left_deque:
            my_l_num += element
        # print my_l_num
        if not eu.primality(int(my_l_num)):
            from_left = 0
        left_deque.popleft()
    while right_deque:
        my_r_num = ''
        # print right_deque
        for element in right_deque:
            my_r_num += element
        # print my_l_num
        if not eu.primality(int(my_r_num)):
            from_right = 0
        right_deque.pop()
    if from_left:
        if from_right:
            return True
    return False

if __name__ == "__main__":
    my_sum = 0
    for x in xrange(8, 800000):
        if eu.primality(x):
            if truncatable(x):
                my_sum += x
    print my_sum