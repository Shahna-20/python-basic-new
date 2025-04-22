#Delete Object Properties

#You can delete properties on objects by using the del keyword:
#Delete the age property from the p1 object ?

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hallo my age is " + self.age)

p1 = Person("john" ,34)

del p1.age
print(p1.age)