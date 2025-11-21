#!/usr/bin/env python3
import sys
if (len(sys.argv) == 1):
    print("none")
else:
    text = sys.argv[1]
    word = "z"
    for value in text:
        if (word in value):
            print("z", end = "")
    if (text.count("z") == 0):
        print("none")
