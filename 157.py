# Add a new item to the original dictionary
# and see that the items list gets updates as well

car = {
    "brand": "Ford",
    "model": "mustang",
    "year":1956,
}
x = car.items()
print(x)

car["color"] = "red"
print(x)