#!/usr/bin/python

# Project Euler
# Problem 39
# Integer Right Triangles


def triangles(side):
    my_sum = 0
    word = word.strip()
    char_list = list(word.upper())
    # print char_list
    for character in char_list:
        my_sum += (ord(character)-64)
        # print (ord(character)-64), ":", my_sum
    return my_sum

if __name__ == "__main__":
    for p in range(1, 1001):
        pass