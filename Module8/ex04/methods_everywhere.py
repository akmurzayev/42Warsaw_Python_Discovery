#!/usr/bin/env python3
import sys

def shrink(argv):
    return(argv[:8])
def enlarge(argv):
    return(argv + "Z"*(8-len(argv)))

if (len(sys.argv) == 1):
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) >= 8:
            print(shrink(arg))
        else:
            print(enlarge(arg))


