#!/usr/bin/python

# Project Euler
# Problem 33
# Digit canceling fractions


from fractions import Fraction


my_product = 1
for denominator in range(10, 100):
    for numerator in range(10, denominator + 1):
        if denominator % 10 == 0 or denominator % 11 == 0:
            continue

        numerator_digit = int(str(numerator)[0])
        denominator_digit = int(str(denominator)[1])

        numerator_digit_2 = int(str(numerator)[1])
        denominator_digit_2 = int(str(denominator)[0])

        if numerator_digit_2 == denominator_digit_2:
            first = Fraction(numerator, denominator)
            second = Fraction(numerator_digit, denominator_digit)

            if first == second:
                print(
                    str(numerator) + "/" + str(denominator) + "\t" + str(first))
                my_product *= first
print(my_product)
