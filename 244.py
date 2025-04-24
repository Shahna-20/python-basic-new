#Add a year parameter,
# and pass the correct year when creating objects ?


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class student(Person):
    def __init__(self, fname, lname , year):
        super().__init__( fname,lname)
        self.graduationyear = year

x = student("mike", "olsen" , 2022)
print(x.graduationyear)