# Decorators

Decorators allow you to "decorate" a function, it allows to tack on extra functionality to an already existing function using the operator `@` and it is placed on top of the original function.

```python
def my_decorator_simple(fn):
  def wrapper():
    print('-- Executed before function received as argument')
    fn()
    print('-- Executed after function received as argument\n')
  return wrapper

def my_decorator_with_params(fn):
  def wrapper(*args, **kargs):
    print('-- Executed before function received as argument')
    fn(*args, **kargs)
    print('-- Executed after function received as argument\n')
  
  return wrapper

@my_decorator_simple
def my_function():
  print('This is a simple function')

@my_decorator_with_params
def my_function_with_params(arg1, arg2):
  print(f'This is the function my_function with args: {arg1} {arg2}')

my_function()
my_function_with_params(arg1=10,arg2=20)

# Result:

# -- Executed before function received as argument
# This is a simple function
# -- Executed after function received as argument
# 
# -- Executed before function received as argument
# This is the function my_function with args: 10 20
# -- Executed after function received as argument
```

In other words, when the operator `@` is utilized it automatically places the function inside other function, so the code above is equivalent to this:

```python
def my_decorator_simple(fn):
  def wrapper():
    print('-- Executed before function received as argument')
    fn()
    print('-- Executed after function received as argument\n')
  return wrapper

def my_decorator_with_params(fn):
  def wrapper(*args, **kargs):
    print('-- Executed before function received as argument')
    fn(*args, **kargs)
    print('-- Executed after function received as argument\n')
  
  return wrapper

def my_function():
  print('This is a simple function')

def my_function_with_params(arg1, arg2):
  print(f'This is the function my_function with args: {arg1} {arg2}')

my_decorator_simple(my_function)()
my_decorator_with_params(my_function_with_params)(arg1=10,arg2=20)

# Result:

# -- Executed before function received as argument
# This is a simple function
# -- Executed after function received as argument
# 
# -- Executed before function received as argument
# This is the function my_function with args: 10 20
# -- Executed after function received as argument
```