#!/usr/bin/env python3
import sys

def downcase_all(arg):
    return(arg.lower())

if (len(sys.argv) == 1):
    print("none")
else:
    for arg in sys.argv[1:]:
        print(downcase_all(arg))
