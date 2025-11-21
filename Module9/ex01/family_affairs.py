#!/usr/bin/env python3

def find_the_redheads(d):
    return (list(filter(lambda name:d[name] == "red", d.keys())))

    
dupont_family = {
    "florian" : "red",
    "marie" : "blond",
    "virginie" : "brunette",
    "david" : "red",
    "franck" : "red"
}
print(find_the_redheads(dupont_family))