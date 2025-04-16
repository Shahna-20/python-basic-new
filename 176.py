# Access Items in Nested Dictionaries
#Print the name of child2

myfamily = {
    "child1" : {
        "name" : "email",
        "year" : 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2008
    },
    "child3": {
        "name": "annu",
        "year": 2005
    }
}
print(myfamily["child2"]["name"])