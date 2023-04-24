#!/usr/bin/python

# Project Euler
# Problem 31
# Coin Sums

cents = 200
denominations = [200, 100, 50, 20, 10, 5, 2, 1]
names = {200: "two-pound(s)", 100: "one-pound(s)", 50: "50p(s)", 20: "20p(s)", 10: "10p(s)", 5 : "5p(s)", 2: "2p(s)", 1 : "1p(s)"}


def count_combs(left, i, comb, add):
    if add:
        comb.append(add)
    if left == 0 or (i+1) == len(denominations):
        if (i+1) == len(denominations) and left > 0:
            comb.append((left, denominations[i]))
            i += 1
        while i < len(denominations):
            comb.append((0, denominations[i]))
            i += 1
        print " ".join("%d %s" % (n, names[c]) for (n, c) in comb)
        return 1
    cur = denominations[i]
    return sum(count_combs(left-x*cur, i+1, comb[:], (x, cur)) for x in range(0, int(left/cur)+1))

print count_combs(cents, 0, [], None)