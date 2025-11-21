#!/usr/bin/env python3

def famous_births(d):
    person_lists=[]

    for key, data in d.items():
        person_lists.append({"name": data["name"], 
                             "year": int(data["date_of_birth"])})
    person_lists = sorted(person_lists, key = lambda x : x["name"])

    person_lists = sorted(person_lists, key = lambda x : x ["year"])
    
    for person in person_lists:
        print(f"{person['name']} : {person ['year']}")


women_scientist = {
    "ada" : { "name" : "Ada Lovelyace", "date_of_birth": "1815"},
    "cecilia" : { "name" : "Cecilia Payne" , "date_of_birth" : "1900"},
    "lise" : {"name" : "Lise Meitner", "date_of_birth" : "1878"},
    "grace" : {"name" : "Grace Hopper", "date_of_birth" : "1906"}
}
famous_births(women_scientist)
