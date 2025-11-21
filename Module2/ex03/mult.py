#!/usr/bin/env python3
first_nbr = int (input ("Enter the first number: "))
second_nbr = int (input ("Enter the second number: "))
result = first_nbr * second_nbr
print (first_nbr , "x", second_nbr , "=", result )
if (result > 0):
	print("The result is positive")
elif (result < 0):
	print("The result is negative")
elif (result == 0):
	print("The result is equal zero")
