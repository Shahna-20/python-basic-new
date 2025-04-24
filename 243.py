#Add Properties
#Add a property called graduationyear to the Student class ?


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class student(Person):
    def __init__(self, fname, lname):
        super().__init__( fname,lname)
        self.graduationyear = 2019

x = student("mike", "olsen")
print(x.graduationyear)