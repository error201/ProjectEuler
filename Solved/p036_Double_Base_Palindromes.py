#!/usr/bin/python

# Project Euler
# Problem 36
# Double-base palindromes

import euler as eu


running_sum = 0
n = 1
while n < 1000001:
    list_n = list(str(n))
    reverse_list_n = list_n[::-1]
    if reverse_list_n == list_n:
        bin_n = bin(n)
        pre_bin_list_n = list(str(bin_n))
        bin_list_n = pre_bin_list_n[2:]
        reverse_bin_list_n = bin_list_n[::-1]
        if reverse_bin_list_n == bin_list_n:
            running_sum += n
    n += 1
print running_sum