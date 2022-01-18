myset = set()

myset.add(1) # adds element to set
myset.add(2)
myset.add(2) # this element will not be added because '2' already is in the set. But no error will be raised

print(myset)

mylist = [1,5,1,1,1,1,1,1,2,2,2,2,3,4,4]
uniquevalues = set(mylist) # casts a list to set, eliminating all duplicated values

print(uniquevalues)