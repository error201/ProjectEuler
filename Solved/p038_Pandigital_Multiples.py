#!/usr/bin/python

# Project Euler
# Problem 38
# Pandigital Multiples


import euler as eu


results = {}
for i in range(1, 9999999 + 1):
    products = []
    j_list = []
    for j in range(1, 9999999 + 1):
        product_length = 0
        for item in products:
            product_length += len(str(item))
        if product_length > 9:
            break
        elif product_length < 9:
            k = i * j
            products.append(k)
            j_list.append(j)
        elif product_length == 9:
            final_digits = ''
            for number in products:
                final_digits += str(number)
            if eu.is_pandigital(int(final_digits)):
                results[final_digits] = (i, j_list)
                print('{0} x {1} == {2}'.format(i, j_list, final_digits))
            break
maximum = 0
for key in results.keys():
    if int(key) > maximum:
        maximum = int(key)
print(maximum)
