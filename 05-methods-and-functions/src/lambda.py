def square(num):
  return num**2

def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False

numbers = range(10)

# Apply functions square on numbers
for e in map(square, numbers):
  print(e)
print()

# lambda function
square2 = lambda num: num ** 2
for e in map(square2, numbers):
  print(e)
print()

# lambda function defined on method argument
print(list(map(lambda num: num**2, numbers)))
print()

# Apply filter is_even on numbers, just returns numbers which is_even function returns True
for e in filter(is_even, numbers):
  print(e)
print()

# Filter with lambda expression
print(list(filter(lambda num: num % 2 == 0, numbers)))

