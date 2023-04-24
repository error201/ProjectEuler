#!/usr/bin/python

# Project Euler
# Problem 63
# Powerful digit counts


count = 0
for x in range(1,100):
    for y in range(1,100):
        res = pow(x, y)
        if len(str(res)) == y:
            print('{0}**{1} = {2}'.format(x, y, res))
            count += 1
print(count)
