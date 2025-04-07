#local variable

def myfunc1():
    z = "fanatastic"
    # z is an local variable, can be accessed only inside function.
    print(z)
    
myfunc1()



#global keyword

def myfunc():
    global  x
    x = "super"
myfunc()
print("python is " + x)