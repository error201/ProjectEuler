#!/usr/bin/python

# Project Euler
# Problem 43
# Sub-string divisibility


from euler import perms


running_sum = 0


for n in perms('1234567890'):
    if int(n[1:4]) % 2 == 0:
        if int(n[2:5]) % 3 == 0:
            if int(n[3:6]) % 5 == 0:
                if int(n[4:7]) % 7 == 0:
                    if int(n[5:8]) % 11 == 0:
                        if int(n[6:9]) % 13 == 0:
                            if int(n[7:10]) % 17 == 0:
                                running_sum += int(n)
                                print(n)
print(running_sum)
