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

def short_hand(short):
    short = short.lower().replace("add","with").replace("&","too").replace("you","U").replace("for","4").replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
    return(short)

statement = input("Type a statement")
short = short_hand(statement)
print(short)

#Remove_case_and_punctuation

def removing(check):
    check = check.lower().replace(" ","").replace(",","").replace(".","").replace(",","")
    return(check)

statement2 = input("Type of sentence")
check = removing(statement2)
print(check)

#palindrome

def palindrome(check):
    check = removing(check)
    return check == check[::-1]

print(palindrome("Madam, I'm Adam"))