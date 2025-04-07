#Remove Whitespace

#whitespace is the space before and/or after the actual text,
# and very often you want to remove this space.

#the strip() method removes any whitespace from the beginning or the end:

a = "  hallo, world!   "
print(a.strip())   #returens "hallo,world"