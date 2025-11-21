#!/usr/bin/env python3
def array_of_names(d):
    list_full = []
    for first, last in d.items():
        list_name = first.capitalize() + " "+ last.capitalize()
        list_full.append(list_name) 
    return (list_full)
    


persons = {
    "jean": "valjean",
    "grace" : "hopper",
    "xavier" : "niel",
    "fifi" : "brindacier"
}
print(array_of_names(persons))