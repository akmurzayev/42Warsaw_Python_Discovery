#!/usr/bin/env python3

usr = input("Give me a number: ")
if "." not in usr:
    print("This number is an integer");
else:
    decimal_part = usr.split(".",1)[1]
    if (decimal_part == "0" * len(decimal_part) ):
        print("This number is an integer");
    else:
        print("This number is a decimal");
