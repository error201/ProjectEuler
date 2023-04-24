#!/usr/bin/python

# Project Euler
# Problem 32
# Pandigital products


import euler as eu


results = {}
for i in range(1, 9999999 + 1):
    products = []
    for j in range(i, 9999999 + 1):
        product_length = 0
        for item in products:
            product_length += sum()
        k = i * j
        if len(str(i)) + len(str(j)) + len(str(k)) < 9:
            continue
        elif len(str(i)) + len(str(j)) + len(str(k)) > 9:
            break
        else:
            digits = [str(i), str(j), str(k)]
            final_digits = ''.join(digits)
            if eu.is_pandigital(int(final_digits)):
                res = "{1} x {2} = {0}".format(k, i, j)
                multiplicands = {i, j}
                print(res)
                if int(k) not in product_sum:
                    product_sum.append(int(k))
print(sum(product_sum))
