"""
title: strings_practice
author: Faryal
date: 2019-06-11 14:51
"""

#character_lab

alphabet = "abcdefghijklmnopqrstuvwxyz"
answer = input("Enter a character")
print(answer in alphabet)

#short_hand

short_hand = "Thank you for that! You are too sweet and kind!"
changes = short_hand.replace("and","&") or short_hand.replace("too","2") or short_hand.replace("you","U") or short_hand.replace("four","4")
print(changes("Thank you for that! You are too sweet and kind!"))