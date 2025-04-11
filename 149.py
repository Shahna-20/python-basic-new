# there is also a method called get()
# that will give you the same result

# get the value of the "model" key

thisdict = {
    "brand": "Ford",
    "model": "mustang",
    "year":1956,
}
x = thisdict.get("model")
print(x)