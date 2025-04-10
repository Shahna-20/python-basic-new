
#The values True and 1 are considered the same value.
# The same goes for False and 0.

#Join sets that contains the values
# True, False, 1, and 0, and see what is considered as duplicates?


set1 = {"apple",1, "banana","cherry",0}
set2 = {False, "google", 1, "apple",2,True}  # True-1

set3 = set1.intersection(set2)

print(set3)

