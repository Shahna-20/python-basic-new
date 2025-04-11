# Make a  change in the original dictionary
# and see that the values list gets updated as well

car = {
    "brand": "Ford",
    "model": "mustang",
    "year":1956,
}

x = car.values()
print(x) # before the change

car["year"] = 2020
print(x) # after the change