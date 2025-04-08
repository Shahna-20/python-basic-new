# Add Any Iterable

# The extend() method does not have to append lists,
# You can add any iterable object (tuples, sets, dictionarize etc.)

#Add elements of a tuple to a list

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)
print(thislist)