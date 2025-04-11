# add a new items to the original dictionary
# and see that the values list gets updated as well:

car = {
    "brand": "Ford",
    "model": "mustang",
    "year":1956,
}

x = car.values()
print(x)

car["color"] = "red"
print(x)