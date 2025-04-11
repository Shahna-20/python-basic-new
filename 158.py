# check if key Exists

# To determine if a specified key is present in
# a dictionary use the in keyword

# check if "model" is present in the dictionary

thisdict = {
    "brand": "Ford",
    "model": "mustang",
    "year":1956,
}

if "model" in thisdict:
    print("yes, 'model' is one of the keys in the thisdict dictionary")
else:
    print("not is thisdict")