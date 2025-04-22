#Modify Object Properties
#You can modify properties on objects like this

#  Set the age of p1 to 40 ?


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hallo my age is " + self.age)

p1 = Person("john" ,34)

p1.age = 40
print(p1.age)
