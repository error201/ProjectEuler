#!/home/jarter/venv3/bin/python

# Project Euler
# Problem 95
# Amicable chains


import euler as eu


my_max = 0
my_collection = []


def sum_it(n):
    return sum(eu.list_factors(n, True))


for j in range(12496, 1000000):
    chain = []
    if eu.is_prime(j):
        continue
    if j in my_collection:
        continue
    chain.append(j)
    new_value = sum_it(j)
    while True:
        if eu.is_prime(new_value):
            break
        if new_value in my_collection:
            break
        if new_value > 1000000:
            break
        if new_value not in chain:
            if eu.is_prime(new_value):
                break
            else:
                chain.append(new_value)
                new_value = sum_it(new_value)
        else:
            if new_value == j:
                for item in chain:
                    if item not in my_collection:
                        my_collection.append(item)
                chain.append(new_value)
                print(j, min(chain), len(chain) - 1, chain)
                break
            else:
                break
