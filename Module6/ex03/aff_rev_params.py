#!/usr/bin/env python3
import sys

if(len(sys.argv) > 2):
    for value in sys.argv[1:]:
        print(value)
elif (len(sys.argv) <= 2):
    print("none")
