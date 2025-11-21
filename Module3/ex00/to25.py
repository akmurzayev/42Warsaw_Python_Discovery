#!/usr/bin/env python3
input_nbr = int (input ("Enter a number less than 25\n"))
if (input_nbr > 25):
	print("Error");
elif (input_nbr < 25):
	while (input_nbr <= 25):
		print("Inside the loop, my variable is ", input_nbr);
		input_nbr += 1
