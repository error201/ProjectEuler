#!/usr/bin/python

counter = 0
item = 0
maximum = 0


def collatz(n):
    global counter
    counter += 1
    if n == 1:
        return
    elif n % 2 == 0:
        n /= 2
        collatz(n)
    else:
        n = (3*n) + 1
        collatz(n)


i = 1000000
while i >= 1:
    counter = 0
    thingy = collatz(i)
    if counter > maximum:
        maximum = counter
        item = i
    i -= 1

print(item, maximum)
