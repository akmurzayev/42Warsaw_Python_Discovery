#!/usr/bin/env python3
import sys
import re

if (len(sys.argv) == 1):
    print("none")
elif (len(sys.argv) > 1):
    usr = input("What was the parameter? ")
    if (sys.argv[1] != usr):
        print("Nope, sorry...")
    elif (sys.argv[1] == usr):
        print("Good job!")
