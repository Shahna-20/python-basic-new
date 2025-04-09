# Another way to join two lists

# is by appending all the items from list2 into list1, one by one.

#Append list2 into list2

list1 = ["a", "b", "c", "d"]

list2 = [1, 2, 3, 4, 5]

for x in list2:
    list1.append(x)

print(list1)