# Create three dictionaries

#then create one dictionary that will contain
# the other three dictionaries

child1 = {
     "name":"Emaa",
    "year": 2004
}
child2 = {
     "name":"liya",
    "year": 2006
}
child3 = {
     "name":"john",
    "year": 204
}
myfamily = {
    "child1": child1,
    "child2" : child2,
    "child3": child3
}
print(myfamily)