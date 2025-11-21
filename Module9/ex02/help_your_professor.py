#!/usr/bin/env python3

def average(d):
    std_average = sum(d.values()) / len(d)
    return (std_average)
    

Class_3B = {
    "marine" : 18,
    "jean" : 15,
    "coline" : 8,
    "luc" : 9
}
Class_3C = {
    "quentin" : 17,
    "julie" : 15,
    "marc" : 8,
    "stephanie" : 13
}
print(f"Average for class 3B: {average(Class_3B)}.")
print(f"Average for class 3C: {average(Class_3C)}.")
