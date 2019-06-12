"""
title: function_practice
author: Faryal
date: 2019-06-12 11:22
"""

#Age_calculator

def age_calculator(current_date, birth_year):
    return current_date - birth_year

current_date = int(input("What year is it?"))
birth_year = int(input("When were you born?"))
print(f"You are " + str(current_date - birth_year) + " years old.")


#Averaging_numbers

def avg_number(x,y,z):
    return (x+y+z)/3

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
print(avg_number(x,y,z))