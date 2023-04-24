#!/usr/bin/python

# Special Pythagorean Triplet

total = 1000

def find_it():
    for first_digit in range(1, 1000):
        a = first_digit
        for second_digit in range(1, 1000):
            b = second_digit
            c = 1000 - (a + b)
            if a**2 + b**2 == c**2:
                if a < b:
                    if b < c:
                        print "a: " + str(a)
                        print "b: " + str(b)
                        print "c: " + str(c)
                        print "product: " + str(a*b*c)
                        break