#Class Polymorphism

#Polymorphism is often used in Class methods,
# where we can have multiple classes with the same method name.

#Different classes with the same method ?


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")


class Boat:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def move(self):
        print("sail")


class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly")

car1 = Car("ford", "mustange")
boat1 = Boat("ibize","tourising20")
plane1 = plane("boeing", "767")


for x in (car1, boat1, plane1):
    x.move()


    # we have three classes: car, boat and plans,
    # and they all have a method called move()
