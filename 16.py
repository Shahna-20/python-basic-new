#Global Variables

#Create a variable outside of a function, and
#use it inside the function & outside the function.

x = "awsome" #scope of x is global

def myfunc():

 print("python is " + x)

myfunc()
print(x)