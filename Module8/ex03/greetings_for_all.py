#!/usr/bin/env python3
import sys

def greetings(name = "noble stranger."):
    if type(name) != str:
        print("Hello, It was not a name.") 
    else:
        print(f"Hello, {name}.")


greetings("Alexndra")
greetings("Will")
greetings()
greetings(42)