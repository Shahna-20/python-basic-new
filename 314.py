#Close Files

#It is a good practice to always
# close the file when you are done with it.

#Close the file when you are finish with it ?


f = open("demofile.txt", "r")

print(f.readline())

f.close()


#Note: You should always close your files,
# in some cases, due to buffering,
# changes made to a file may not show until you close the file.