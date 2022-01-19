list1 = range(3)
list2 = ['a', 'b', 'c']
list3 = ['!', "@", "#"]

for e in zip(list1, list2, list3):
  print(e)

for a,b,c in zip(list1, list2, list3):
  print(f'the value of a is {a}, the value of b is {b}, the value of c is {c},')