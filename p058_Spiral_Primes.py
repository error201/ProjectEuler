#!/usr/bin/python

# Project Euler
# Problem 58
# Spiral Primes


import numpy as np


def count_primes(spiral):
    pass


class Spiral():

    def __init__(self, start_num=0, size_num=1):
        self.start = start_num
        self.size = size_num
        self.data = np.array([[start_num]])
        self.height, self.width = self.data.shape

    def display(self):
        print(self.data)

    def grow(self, size_num):
        # right
        current_height = self.height
        current_max = np.argmax(self.data)
        new_list = [x for x in range(current_max, current_height)]
        new_list.reverse()
        new_vector = np.array(new_list)
        new_vector.T
        new_matrix = np.hstack(self.data, new_vector)
        self.data = new_matrix

if __name__ == "__main__":
    a = Spiral(start_num=1)
    a.display()
