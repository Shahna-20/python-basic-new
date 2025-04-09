
#Using Asterisk (*)

#If the number of variables is less than the number of values,
# you can add an * to the variable name
# and the values will be assigned to the variable as a list

#Assign the rest of the values as a list called "red":

fruits = ("apple","banana","cherry", "strawberry","orange")

(green, yellow, *red) =fruits

print(green)
print(yellow)
print(red)