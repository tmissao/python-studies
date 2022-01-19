mylist = [1,2,3,4,5]

for e in mylist:
  pass

for e in mylist:
  if e == 3:
    continue
  print(e)

print()

for e in mylist:
  if e == 3:
    break
  print(e)

print()

index = 0
while index < 5:
  if index == 3:
    break
  print(index)
  index += 1