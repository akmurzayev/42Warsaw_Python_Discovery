#!/usr/bin/env python3
import sys

if(len(sys.argv) == 1):
    print("none")
else:
    word = "ism"
    text = sys.argv[1:]
    for value in text:
        if(value.endswith(word) ):
            continue
        else:
            print(value + word)