#!/usr/bin/env python3
import sys
import re
if (len(sys.argv) <= 2):
    print("none")
else:
    word1 = sys.argv[1]
    word2 = sys.argv[2]
    counter = len(re.findall(rf"\b{word1}\b" ,word2))
    if (counter > 0):
        print(counter)
    else:
        print("none")
