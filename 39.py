

# You can use index numbers{0}
# to be sure the arguments are placed in the correct placeholders:
#from


quantity = 3
itemno = 567
price = 49.95

myorder = "i want {2} pieces of item {0} for {1} dollars"


print(myorder.format(quantity, itemno, price))