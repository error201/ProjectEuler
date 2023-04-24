#!/usr/bin/python

# Project Euler
# Problem 59
# XOR decryption


import binascii
import math
import os

import itertools as tools


def make_code_points():
    # Create a list of all possible keys
    raw_codes = [list(x) for x in tools.combinations_with_replacement(
        'abcdefghijklmnopqrstuvwxyz', 3)]
    my_codes = []
    ascii_codes = []
    for item in raw_codes:
        replaced_code = [x.encode('ascii') for x in item]
        my_codes.append(replaced_code)
    for item in my_codes:
        replaced_code = [int(x.hex(), 16) for x in item]
        ascii_codes.append(replaced_code)
    return ascii_codes


def make_strand(code_list, n):
    template_length = len(code_list)
    repetition = math.ceil(n / template_length)
    sub_key = []
    for i in range(0, repetition):
        for item in code_list:
            sub_key.append(item)
    return sub_key[0:n]


def my_decode(key_point_list, code_point_list):
    my_tuples = zip(key_point_list, code_point_list)
    new_list = [(a ^ b) for a, b in my_tuples]
    hexed_list = [hex(x) for x in new_list]
    encoded_list = [bytes.fromhex(x[2:4]) for x in hexed_list]
    decoded = ''.join(x.decode('ascii') for x in encoded_list)
    if decoded.isprintable():
        return decoded

if __name__ == '__main__':
    my_fname = os.path.join(os.getcwd(), r'p059_Ciphertext.txt')
    my_file = open(my_fname, 'r')
    ciphertext = my_file.read()
    first_ten = [int(x) for x in ciphertext.split(',')[0:40]]
    my_keys = make_code_points()
    for item in my_keys:
        my_strand = make_strand(item, 40)
        decoded_string = my_decode(my_strand, first_ten)
        if decoded_string:
            print(item, decoded_string)
