#!/usr/bin/env python3
usr = input("Give me a number: ")
if  "." not in usr:
	print(usr)
else:
    decimal = usr.split(".",1)[1]
    integer = usr.split(".",1)[0]
    if(decimal == "0" * len(decimal)):
        print(integer)
    else:
        print(int(integer) + 1)
