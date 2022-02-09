def add(n1, n2):
   return n1 + n2

number1 = 10
number2 = '20'

try:
  result = add(number1, number2)
# Executed with an error happen, when a type of error is not passed, all error are captured
except:
  print('An error ocurred calling the method add')
# else is optional and just is executed if an error did not happen
else:
  print(f'Add went well the result is {result}')

try:
  f = open('testfile', 'r')
  f.write('Write a test line')
except TypeError:
  print('There was a type error!')
except OSError:
  print('Hey you hava an OS error')
except:
  print('A generic error happened')
# finally is optional always executed if an error happens or not
finally:
  print('I always run')