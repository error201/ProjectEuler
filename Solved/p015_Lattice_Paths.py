#!/usr/bin/python

# Catalan Numbers


def factorial(n):
    product = 1
    for number in range(1, n+1):
        product *= number
    return product


def num_paths(grid_size = 20):
    return factorial(2 * grid_size) / (factorial(grid_size)) ** 2


if __name__ == "__main__":
    print(num_paths())
