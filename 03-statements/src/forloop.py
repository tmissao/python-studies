mylist = [1,2,3,4,5,6,7,8,9,10]

for e in mylist:
  print(e)

print()

# Checks by even number
for e in mylist:
  if e % 2 == 0:
    print(f'The number {e} is even')
  else:
    print(f'The number {e} is odd')

# Sums the list values
list_sum = 0
for e in mylist:
  list_sum += e
print(f'The sum of the list is: {list_sum}\n')

# Iterates over string characters
mystring = 'hello world'
for e in mystring:
  print(e)

# Uses '_' when you do not care about the element in the list
for _ in mylist:
  print('Looping')

# Tuples
tup = (10,20,30)
for e in tup:
  print(e)

# Tuple Packing
tuppleList = [(10,20), (30,40), (50,60), (70,80)]
for (a,b) in tuppleList:
  print(f'The value of a is {a}, the value of b is {b}')

print()

for a,b,c in [(1,2,'a'), (3,4,'b'), (5,6,'c')]:
  print(f'The value of a is {a}, the value of b is {b}, the value of c is {c}')

print()

# Dictionary
d = {'k1': 1, 'k2': 2, 'k3': 3}
for k in d: # by default just the key is returned in the for loops using dictionaries
  print(f'The value of k is {k}')

print()

for k,v in d.items(): # to iterate over key and its value calls the items() method that return a tuple
  print(f'The value of k is {k}, the value of v is: {v}')