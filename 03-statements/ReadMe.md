# Statements

## Control Flow
---
Controls when a certain code should be executed, this is determined when a particular condition has been met. On python the keywords `if`, `elif`, `else` is used to implement this logic.

> Control flows syntax makes use of colons and indentation (whitespace)

- `if`
```python
istrue = True

if istrue:
  print('The condition is true')
```

- `else`
```python
istrue = False

if istrue:
  print('The condition is true')
else:
  print('The condition is false')
```

- `elif`
```python
firstCondition = False
secondCondition = False

if firstCondition:
  print('The first condition is true')
elif secondCondition:
  print('The second condition is true')
else:
  print('None of conditions is true')
```

## For Loops
---
Many objects in Python are iterable, meaning that is possible to iterate over every element in the object, like: lists, strings, tuples and much more

```python
mylist = [1,2,3]
mystring = 'hello world'

# Iterates over the list
for e in mylist:
  print(e)

# Checks if the element of the list is even or odd
for e in mylist:
  if e % 2 == 0:
    print(f'The number {e} is even')
  else:
    print(f'The number {e} is odd')

# Iterates over the string characters
for e in mystring:
  print(e)

# Uses '_' when you do not care about the element in the list
for _ in mylist:
  print('Looping')

# Tuples
tup = (10,20,30)
for e in tup:
  print(e)

# Tuple Packing
tuppleList = [(10,20), (30,40), (50,60), (70,80)]
for a,b in tuppleList: # Python unpacks the tuples values into the a and b variables
  print(f'The value of a is {a}, the value of b is {b}')

for a,b,c in [(1,2,'a'), (3,4,'b'), (5,6,'c')]: # Python unpacks the tuples values into the a, b and c variables
  print(f'The value of a is {a}, the value of b is {b}, the value of c is {c}')

# Dictionary
d = {'k1': 1, 'k2': 2, 'k3': 3}
for k in d: # by default just the key is returned in the for loops using dictionaries
  print(f'The value of k is {k}')

for k,v in d.items(): # to iterate over key and its value calls the items() method that return a tuple
  print(f'The value of k is {k}, the value of v is: {v}')
```
## While Loops
---

While loops will continue to execute a block of code while some condition remains true

```python
mylist = [1,2,3,4]

index = 0
while index < len(mylist):
  print(mylist[index])
  index += 1

while True:
  print('it runs forever')

# While loop if an else condition (else run right after the while condition fails)
x = 0
while x < 5:
  print(f'The current value of x is {x}')
  x += 1
else:
  print('X is no longer less than 5')
```

## Loops Keywords
---

During loops there are three special keywords:

- `break` - Breaks out the current closest enclosing loop
- `continue` - Goes to the top of the closest enclosing loop
- `pass` - Does nothing at all

```python
mylist = [1,2,3,4,5]

# does not at all, however avoids syntax error
for e in mylist:
  pass

# skips to the next element (avoiding to execute the for commands) when the element is equal to 3
for e in mylist:
  if e == 3:
    continue
  print(e)

# ends the for loop when the element is equal to 3, no further element will be evaluated
for e in mylist:
  if e == 3:
    break
  print(e)

index = 0
while index < 5:
  if index == 3:
    break
  print(index)
  index += 1
``` 

## List Comprehensions
---

In order to shorter code, python uses list comprehensions
```python
# Long way for
mylist = []
for e in range(11):
  mylist.append(e)

# shorter for using list comprehension
mylist = [ e for e in range(11) ]

# shorter for with condition filter (just get even number)
even = [ e for e in range(11) if e % 2 == 0 ]

# shorter for with condition filter (just get odd number) and return logic (power of the element)
odd_pow = [ e ** 2 for e in range(11) if e % 2 == 1 ] 

# shorter if else logic
even_or_odd = [ 'even' if e % 2 == 0 else 'odd' for e in range(11) ]
print(even_or_odd)

# celsius  to fahrenheit
celsius  = [0, 10, 20, 34.5]
fahrenheit = [ ( (9/5)*e + 32 ) for e in celsius  ]
```