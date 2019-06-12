"""
title: random_practice
author: Faryal
date: 2019-06-12 09:53
"""
import random
name = input("Hello! What is your name?")
salary = int(input("What is your salary?"))
print(f"{name}, your current salary is {salary}")
raise_per = (random.randint(0,100))
added_amount = salary * (raise_per/100)
raise_amount = salary + added_amount
print(f"Your raise is {raise_per}% of ${salary}")
print(f"{name}, your new salary is {raise_amount}")