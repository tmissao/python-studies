def create_cubes(n):
  result = []
  for x in range(n):
    result.append(x**3)
  return result

# This way is memory efficient since it does not allocate all the size necessary to create the n cubes,
# it generates a value and sent it, and waits until the next value is required
def create_cubes_generator(n):
  for x in range(n):
    yield x**3

def fibonacci(n):
  a = b = 1
  for _ in range(n):
    yield a
    a,b = b,a+b

for x in create_cubes(10):
  print(x)

for x in create_cubes_generator(10):
  print(x)

for x in fibonacci(10):
  print(x)

iterator = fibonacci(10)
while True:
  try:
    value = next(iterator)
    print(value)
  except StopIteration:
    break


value = "My Amazing String"
iterator = iter(value)
while True:
  try:
    value = next(iterator)
    print(value)
  except StopIteration:
    break


def squares(n):
  return (e**2 for e in range(n))

for x in squares(10):
  print(x)