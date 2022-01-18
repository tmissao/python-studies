my_list = [1,2,3]
mix_list = ['string', 12, 15.46]
mix_list_len = len(mix_list) # get list length

print(my_list)
print(mix_list)
print(mix_list_len)

print(my_list[0]) # indexing
print(my_list[1:]) # slicing
print(my_list + mix_list) # concatenates to a new list

my_list[0] = 10 # lists unlike strings are not immutable
print(my_list)

# Lists Common Methods
my_list.append(4) # adds an element on the end of the list
print(my_list) 
my_list.pop() # removes the last element of the list
print(my_list)
my_list.pop(0) # removes the first element of the list
print(my_list)

str_list = ['a', 'e', 'x', 'b', 'c' ]
num_list = [4, 1, 8, 3]

str_list.sort() # sorts a list
print(str_list)

num_list.reverse() # reverts a list
print(num_list)