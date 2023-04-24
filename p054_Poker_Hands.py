#!/home/jarter/venv3/bin/python

# Project Euler
# Problem 54
# Poker hands


import re


three_oak = re.compile(
    "(?:(?P<card>\S)\w).{0,7}(?P=card).{0,7}(?P=card)"
)
four_oak = re.compile(
    "(?:(?P<card>\S)\w).{0,5}(?P=card).{0,5}(?P=card).{0,5}(?P=card)"
)


Numerary = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8,
            '7': 7,  '6': 6,  '5': 5,  '4': 4,  '3': 3,  '2': 2}


def card_sort(hand):
    hand_dict = {}
    for card in hand:
        pass


hands = open(r'c:\temp\Euler\p054_Poker_Results.txt', 'r')
for hand in hands:
    clean_hand = hand.strip()
    hand_list = list(clean_hand.split(' '))
    player1_hand = hand_list[:5]
    player2_hand = hand_list[5:]
    print(player1_hand)
