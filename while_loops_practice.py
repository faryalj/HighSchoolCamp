"""
title: while_loops_practice
author: Faryal
date: 2019-06-13 14:53
"""
x = 10
while(1 <= x <= 10):
    print(x, end = " ")
    x-= 1

print()
print("=" * 30)

x_input = input("Enter an integer that is greater than 0:")
while x_input <= "0":
    print("Waiting")
    x_input = input("Enter an integer that is greater than 0:")

print("Thanks for inputting!")

print()
print("=" * 30)

print("Enter two integers, the first smaller than the second")
integer_input1 = int(input("Enter the first integer:"))
integer_input2 = int(input("Enter the second integer"))
while integer_input1 >integer_input2:
    second = int(input("Invalid response. Enter a second number:"))
while (integer_input1<= integer_input2):
    print(integer_input1)
    integer_input1 +=1

