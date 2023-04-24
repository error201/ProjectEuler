#!/usr/bin/python

# Project Euler
# Problem 92
# Square Digit Chains


my_count = 0


def chain(n):
    num_string = str(n)
    num_list = [(int(x))**2 for x in num_string]
    new_num = sum(num_list)
    if new_num == 89:
        global my_count
        my_count += 1
        return
    elif new_num == 1:
        return
    else:
        chain(new_num)


for num in range(2, 10000001):
    chain(num)
print(my_count)
