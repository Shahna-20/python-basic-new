#Object Methods
#Objects can also contain methods.
# Methods in objects are functions that belong to the object.

#create a method in the Person class?
#Insert a function that prints a greeting, and execute it on the p1 object ?


class Person:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def myfunc(abc):
        print("hallo my name is " + abc.name)

p1 = Person("john", 34)
p1.myfunc()