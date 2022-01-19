condition = False

if condition:
  print('condition is True')
else:
  print('condition is not true')

number = 7

if number % 5 == 0:
  print(f'Number {number} is multiple of 5')
elif number % 3 == 0:
  print(f'Number { number } is multiple of 3')
elif number % 2 == 0:
  print(f'Number {number} is multiple of 2')
else:
  print(f'Number {number} is not multiple of 5,3 or 2')

name = 'Josh'

if name == 'Sammy':
  print('Hello Sammy')
  print('How are your kids?')
elif name == 'John':
  print('What`s up John?')
else:
  print('How are you man?')
  print('Are you lost?')
  print('Do you need any help?')