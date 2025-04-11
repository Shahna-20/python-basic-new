# Add a new item to the original dictionary.
# and see that the keys list gets updated as well

car = {
    "brand": "Ford",
    "model": "mustang",
    "year":1956,
}
x = car.keys()
print(x)  # before the change

car["color"] = "white"
print(x) # after the change