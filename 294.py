#Raise a TypeError if x is not an integer ?

x = "hallo"

if not type(x) is int:
    raise TypeError("Only integers are allowed")