# Operators

Python has a rich set of useful operations like:

## Range
---

Generates sequences of iterable object

```python
# generates numbers from 0 to stop argument (not inclusive)
for num in range(10):
  print(num)

# generates numbers from start to stop argument (not inclusive), incrementing by 1
for e in range(2, 10):
  print(e)

# generates numbers from start to stop argument (not inclusive), incrementing by step argument
for e in range(2,10,2):
  print(e)

# creates a list using range operator
mylist = list(range(0,11,2))
```

## Enumerate
---
Adds a count to the iterable object
```python
for e in enumerate(word):
  print(e)

# (0, 'H')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')
# (5, '!') 

for i, e in enumerate(word):
  print(f'The value i is {i}, the value of e is {e}') 

# The value i is 0, the value of e is H
# The value i is 1, the value of e is e
# The value i is 2, the value of e is l
# The value i is 3, the value of e is l
# The value i is 4, the value of e is o
# The value i is 5, the value of e is !
```

## Zip
---
Creates a tuple with n values merging n lists
```python
list1 = range(3)
list2 = ['a', 'b', 'c']
list3 = ['!', "@", "#"]

for e in zip(list1, list2):
  print(e)

for a,b,c in zip(list1, list2, list3):
  print(f'the value of a is {a}, the value of b is {b}, the value of c is {c},')
```

## In/not in
---
`in` Returns true if a sequence with the specified value is present in the object

`not in` Returns true if a sequence with the specified value `is not` present in the object
```python
mylist = range(10)
word = "hello world"
dict = { 'key1': 345, 'key2': 678 }

if 5 in mylist:
  print('5 is in the list')

if 10 not in mylist:
  print('10 is not in the list')

if 'ell' in word:
  print('ell is in the word')

if 'word' not in word:
  print('word is not in the word')

if 'key1' in dict:
  print('key1 is in the dictionary')

if 'key' not in dict:
  print('key is not in the dictionary')
```

## Min/Max
---
`min` returns the minimum value of a iterable

`max` returns the maximum value of a iterable

```python
mylist = range(10)

print(f'the minimum value is {min(mylist)}')
print(f'the maximum value is {max(mylist)}')

```

## Random Library
---
Useful random methods
- `shuffle` - shuffles a list
```python
from random import shuffle

mylist = list(range(10))
shuffle(mylist)

print(mylist)
```

- `randint` - generates a random int
```python
from random import randint

print(randint(0,100))
```

## Inputs
---
Allow python programs to accept user inputs:

```python
name = input('Whats your name? ')
string_number = input('Enter a number ')
number = int(string_number)

print(f'Hello {name}, your number is {number}')
```