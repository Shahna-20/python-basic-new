# The Break Statement

# with the break statement we can stop the loop before
# it has looped through all the items:

# exite the loop when x is "bannana"

fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break