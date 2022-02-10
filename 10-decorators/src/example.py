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