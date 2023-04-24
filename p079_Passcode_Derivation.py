#!/usr/bin/python

# Project Euler
# Problem 67
# Maximum Path Sum II


from collections import Counter


keylog = open('c:/Users/jarter/PycharmProjects/Euler/p079_keylog.txt', 'r').readlines()
attempts = [int(x.strip()) for x in keylog]
pattern_count = Counter(attempts)
print(pattern_count.most_common(25))
