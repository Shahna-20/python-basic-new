#Create an Iterator
#To create an object/class as an iterator you have to
#implement the methods _iter() and __next_() to your object.

#Create an iterator that returns numbers,
# starting with 1,
# and each sequence will increase by one (returning 1,2,3,4,5 etc.) ?


class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myobject = MyNumbers()
myiter = iter(myobject)

print(next(myiter))  # 1
print(next(myiter))  # 2
print(next(myiter))  # 3
print(next(myiter))  # 4
print(next(myiter))  # 5
print(next(myiter))  # 6


