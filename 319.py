# create an txt file named work.txt?
# add 5 lines using write ?
# add 2 lines to end using append?
# print first 4 lines using readline()?
# overwrite using another 2 lines?
#last read all

#1
# f = open("work1.txt", "x")

#2
#f = open("work.txt", "w")
#f.write("first line\n second line\n third line\n fouth line\n fifth line")

#3
# f = open("work.txt", "a")
# f.write("first append\n second append")

#4
#f = open("work.txt", "r")
#print(f.readline())
#print(f.readline())
#print(f.readline())
#print(f.readline())
#f.close()


#5
f = open("work.txt", "w")
f.write("first line \n second line")
f.close()

#last
f = open("work.txt", "r")
print(f.read())

f = open("mywork.txt", "x")

