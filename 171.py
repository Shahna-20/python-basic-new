#Loop through both keys and values
#by using the items() method

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
}

for x, y in thisdict.items():
    print(x, y)