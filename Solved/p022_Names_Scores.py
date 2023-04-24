#!/usr/bin/python

# Project Euler Problem 22


def name_score(list_name):
    my_sum = 0
    stringed_name = str(list_name)
    trimmed_name = stringed_name.rstrip('\n')
    char_list = list(trimmed_name)
    for letter in char_list:
        letter_value = (ord(letter))-64
        print(letter + ": " + str(letter_value))
        my_sum += letter_value
    return my_sum

if __name__ == "__main__":
    my_sum = 0
    name_file = open(r'/home/jarter/python/Euler/p022_Name_List.txt', 'r')
    name_list = name_file.readlines()
    name_list.sort()
    for line_number, name in enumerate(name_list):
        current_name_score = name_score(name)
        line_score = (line_number + 1) * current_name_score
        my_sum += line_score
        print(str(line_number + 1) + ": " + name + ", " + str(current_name_score) + ", " + str(line_score) + ", " +
              str(my_sum))
    print(my_sum)

