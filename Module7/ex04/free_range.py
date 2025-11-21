#!/usr/bin/env python3
import sys

try:
    if(len(sys.argv) == 3):
        text = sys.argv[1:]
        nbr1 = int(text[0])
        nbr2 = int(text[1])
        if (nbr1 >= nbr2):
            print("none")
        else:
            nbr3 = list(range(nbr1, nbr2+1))
            print(nbr3)
    else:
        print("none")
except:
    print("none")