#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
elif len(sys.argv) > 1:
    for value in sys.argv[1:]:
        print(value.upper(), end = " ")
