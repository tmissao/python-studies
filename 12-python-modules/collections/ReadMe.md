# Collections

Python has a series of built-in collections ready to use, there are extension of the basic data structures like arrays, tuples, and dictionaries

## Counter
---
Used to count the elements of a list or string

```python
from collections import Counter

mylist = [1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,5,5,5,7,4,5,7,4, 'a']

# Counter is 
counter = Counter(mylist)

for x,y in counter.items():
  print(f'number of element {x}: {y}')

# Get the first two most common element
print(counter.most_common(2))

# Counts letters
counter = Counter('hello my beautiful python world!')
print(counter)

# Counts words
counter = Counter('This is how python can count word, this is awesone!'.split())
print(counter)
```

## Default Dictionary
---

Allows to set a default value if accessing a key that does not exist, on the normal dictionary an error will be raised

```python
from collections import defaultdict

# uses a lambda function to set a default value
d = defaultdict(lambda: 0)

d['correct'] = 100

print(f'the value of correct is: {d["correct"]}')

# On default dict this will raised an error 
print(f'the value of wrong is: {d["wrong"]}')
```

## Named Tuple
---

Named tuple is an extension of the tuple, on default tuple we just have an index relation with the element, however on named tuple it is possible to create a "string" relationship with the element (almost like a dictionary)

```python
from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sammy = Dog(age=5, breed='Husky', name='Sam')

print(sammy.age)
print(sammy[0])

print(sammy.breed)
print(sammy[1])

print(sammy.name)
print(sammy[2])

age,breed,name = sammy
print(age)
print(breed)
print(name)

```