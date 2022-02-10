# Generators

Generator functions allow to write a function that can send back a value and then later resume to pick up where it left off. This is possible to create a generator using the `yield` statement.

In other words, it just generates the value when needed.

```python
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

for x in create_cubes(10):
  print(x)

for x in create_cubes_generator(10):
  print(x)

# yield also can be used in the middle of the function
def fibonacci(n):
  a = b = 1
  for _ in range(n):
    yield a
    a,b = b,a+b

for x in fibonacci(10):
  print(x)
```

Another way to iterate over the generator function is calling the `next` method. So in this way, the function keeps generating the value until an error `StopIteration` is raised, meaning the end of the generator.

```python
iterator = fibonacci(10)
while True:
  try:
    value = next(iterator)
    print(value)
  except StopIteration:
    break
```

Another useful function it the `iter` which gives an iterator object. Useful to iterate over strings, arrays and much more

```python
value = "My Amazing String"
iterator = iter(value)
while True:
  try:
    value = next(iterator)
    print(value)
  except StopIteration:
    break
```

## Generator Comprehension

Likewise list, generator can use comprehension in order to quick create it.

```python
def squares(n):
  # generator comprehension
  return (e**2 for e in range(n))

for x in squares(10):
  print(x)
```