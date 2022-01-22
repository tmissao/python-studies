# Functions
Functions on Python is a way to organize pieces of code, and are created using the keyword `def` with correct indentation and structure

```python
# Basic function
def my_function():
  '''
  Docstring explains function
  '''
  print('Hello')

# Function with args
def my_function_with_name(name):
  print(f'Hello {name}')

# function with default args
def my_function_with_default_value(name='unknown'):
  print(f'Hello {name}')

# returning function
def add_values(num1, num2):
  return num1+num2

# checks if any number is even
def is_any_number_even(numbers):
  for e in numbers:
    if e % 2 == 0:
      return True
  return False

# gets the even numbers
def get_even_number(number):
  return [e for e in number if e % 2 == 0]

# get min and max of list returning a tuple with the min e max value
def get_min_max(numbers):
  min = max = None
  if len(numbers) == 0:
    return (min, max)
  else:
    min = max = numbers[0]
  for e in numbers:
    if e > max:
      max = e
    if e < min:
      min = e
  return (min, max)

# Executes the function
my_function()

# Executes the function with args
my_function_with_name('Missao')

result = add_values(10, 5)
print(f'my result is: {result}')

# Tuple unpack on variable assign
min, max = get_min_max([1,5,-4,10,-20,17,54,-3,8])
print(f'The min value is: {min}, the max value is: {max}')
```

# Special Args
---
On python there are two special args, known as: `*args` and `**kwargs` 

- `*args` - allow to receive an arbitrary number of args (n args), the params received are treated as `tuples`
```python
def myfunc(*args):
  return sum(args) * 0.05

def min(*args):
  if len(args) == 0: 
    return None
  min = args[0]
  for e in args:
    if e < min: min = e
  return min

print(myfunc(40,60,100,200,500))
print(myfunc(40,60,100,200))

print(min(40,60,100,200,500, 0))
print(min())
```

- `**kwargs` - allow to receive an arbitrary number of args (n args), the params received are treated as a `dictionary`
```python
def myfunc(**kwargs):
    if 'model' in kwargs:
      print(f'the model received is {kwargs["model"]}')

myfunc(brand='Ford', year = '1964', model = 'mustang')
``` 


# Methods

Methods are built-in functions inside an object. In order to get explanation about an object or method in python is possible to use the `help()` function

```python
mylist = list(range(10))

# prints list doc
help(mylist)

# prints list append method doc
help(mylist.append)
```

## References

- [`Python Documentation`](docs.python.org/3)