def my_function():
  '''
  Docstring explains function
  '''
  print('Hello')

def my_function_with_name(name):
  print(f'Hello {name}')

# function with default value
def my_function_with_default_value(name='unknown'):
  print(f'Hello {name}')

def add_values(num1, num2):
  return num1+num2

def is_even(num1):
  return num1 % 2 == 0

def is_any_number_even(numbers):
  for e in numbers:
    if e % 2 == 0:
      return True
  return False

def get_even_number(number):
  return [e for e in number if e % 2 == 0]

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

my_function_with_default_value('Missao')
my_function_with_default_value()

result = add_values(10, 5)
print(f'my result is: {result}')

print(is_even(10))
print(is_even(11))
print(is_any_number_even(list(range(1,20,2))))
print(is_any_number_even([1,3,5,7,8,0,11]))
print(get_even_number(list(range(1,20,2))))
print(get_even_number([1,3,5,7,8,0,11]))
print()
print(get_min_max([]))
print(get_min_max([1]))
min, max = get_min_max([1,5,-4,10,-20,17,54,-3,8])
print(f'The min value is: {min}, the max value is: {max}')