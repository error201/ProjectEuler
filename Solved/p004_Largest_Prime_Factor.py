#!/usr/bin/python

products = []
palindromes = []


def check_pal(item):
    a = str(item)
    b = list(a)
    if len(b) == 2:
        one = b[0]
        two = b[1]
        if one == two:
            palindromes.append(item)
    if len(b) == 3:
        one = b[0]
        two = b[1]
        three = b[2]
        if one == three:
            palindromes.append(item)
    if len(b) == 4:
        one = b[0]
        two = b[1]
        three = b[2]
        four = b[3]
        if (one == four) and (two == three):
            palindromes.append(item)
    if len(b) == 5:
        one = b[0]
        two = b[1]
        three = b[2]
        four = b[3]
        five = b[4]
        if (one == five) and (two == four) and (three == two):
            palindromes.append(item)
    if len(b) == 6:
        one = b[0]
        two = b[1]
        three = b[2]
        four = b[3]
        five = b[4]
        six = b[5]
        if (one == six) and (two == five) and (three == four):
            palindromes.append(item)


for x in range(999, 0, -1):
    for y in range(x, 0, -1):
        c = x * y
        check_pal(c)

print(max(palindromes))
