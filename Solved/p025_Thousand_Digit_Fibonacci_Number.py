#!/usr/bin/python

# Project Euler
# Problem 25 - 1000 digit Fibonacci Number

from euler import fibonacci_gen as fibgen

if __name__ == '__main__':
    for index, number in fibgen(10000000):
        my_list = list(str(number))
        list_len = len(my_list)
        if list_len == 1000:
            print str(index+1) + ' : ' + str(list_len)
            break

