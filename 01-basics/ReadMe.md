# Python Basics

## Numbers
---

Currently python works with the following structures representing numbers

- Integers - which are whole numbers
- Floating Point - which are numbers with a decimal

> Python follow the rules of all major languages when performing math ( +, -, *, / ). Otherwise, if you would like to perform a `power operation` you can use the operator `**`

```python
print( 5 ** 2 )
print( 25 **(1/2) )
```

## Variables Assignments
---

Python uses `Dynamic Typing`, so it is possible to reassign variables to different data types.

```python
my_dogs = 2
my_dogs = [ "Fox", "Farofa" ]
print(my_dogs)
```

However, python provides the function `type()` in order to get the variable type

```python
my_dogs = 2
print(type(my_dogs))
my_dogs = [ "Fox", "Farofa" ]
print(type(my_dogs))
```

## Strings
---

Strings are sequences of characters, using the syntax of either single quotes or double quotes
```python
msg = 'hello'
msg2 = "Hello"
msg3 = "Hello world"
```

Since Strings are ordered sequences it is possible using `indexing` and `slicing` to grab sub-sections of the string

```python
# Indexing
msg = "Hello"
print(msg[0])

# Reverse Indexing
print(msg[-1]) # gets the last element of a string

# Slicing (start : end : step)
print(msg[1:]) # Substring starting on index 1
print(msg[1:3]) # Substring starting on index 1 and ending on 3 (not inclusive)
print(msg[:3]) # Substring starting on the beggining and ending on 3 (not inclusive)
print(msg[::2]) # Substring starting on the beggining to the end, but steping by two
```

Also, string types has custom methods

```python
name = "Sam"
print("P" + name[1:]) # String Concatenation
print(name.upper()) # Upper Case String
print(name.lower()) # Lower Case String
print(name.split("a")) # split string into a list based on a specific value
```

## String Formatting
---

Python offers two methods to formatting strings:

- `.format` - built-in method
```python
# The '{}' is evaluated in order by default
print('The {} {} {}'.format('fox', 'brown', 'quick'))

# The '{}' can be accessed using indexing
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))

# The '{}' can use keywords to retrieve values
print('The {f} {b} {q}'.format(f='fox', b='brown', q='quick'))

# Formating floating numbers "{value:width.precision f}"
result = 0.1287001287001287
print('The result is: {r:1.3f}'.format(r=result))

```
- `f-strings` - formatted string literals
```python
name = "Tiago"
surname = "Missão"
result = 0.1287001287001287

print(f'Hello my first name is {name}, and last name {surname}')
print(f'the result is {result:1.3f}')
```

## Lists
---
List are ordered sequences that can hold a variety of object types, also supports `indexing`, `slicing` and can be nested. Is good to remember that, lists unlike strings are not immutable
```python
my_list = [1,2,3]
mix_list = ['string', 12, 15.46]
mix_list_len = len(mix_list) # get list length

print(my_list)
print(mix_list)
print(mix_list_len)

print(my_list[0]) # indexing
print(my_list[1:]) # slicing
print(my_list + mix_list) # concatenates to a new list

# lists unlike strings are not immutable
my_list[0] = 10
print(my_list)

# Lists Common Methods
my_list.append(4) # adds an element on the end of the list
print(my_list) 
my_list.pop() # removes the last element of the list
print(my_list)
my_list.pop(0) # removes the first element of the list
print(my_list)

str_list = ['a', 'e', 'x', 'b', 'c' ]
num_list = [4, 1, 8, 3]

str_list.sort() # sorts a list
print(str_list)

num_list.reverse() # reverts a list
print(num_list)
```

## Dictionaries
---

Dictionaries are unordered mappings for storing objects. This key-value pair allows users to quickly grab objects without needing to know an index location
```python
dict = { 'key1' : 'value1', 'key2' : 'value2' }

print(dict)
print(dict['key2']) # retrieves a value using the dictionary's key

d = { 'k1': 123, 'k2': [0,1,2], 'k3': {'insideKey': 1000}}
print(d['k1'])
print(d['k2'][2])
print(d['k3']['insideKey'])

d['k4'] = 300 # adds a new key-value on dictionary
d['k1'] = 200 # updates a value on dictionary
print(d)

# Dictionary methods
print(d.keys()) # returns all keys of the dictionary
print(d.values()) # returns all values of the dictionary
print(d.items()) # returns all key-value of the dictionary together
```

## Tuples
---
Tuples are very similar to lists. However they have one key difference, they are `immutable`. Once an element is inside a tuple, it can not be reassigned
```python
t = (1, 2, 3)
print(t)

# indexing
print(t[0])
print(t[1:])

# Tuple Methods
t = ('a', 'a', 'b')
print(t.count('a')) # count how many times an elements appers
print(t.index('a')) # returns the index of the first an element appers

# Cannot Perform Assignment
t[0] = 'b' # Error Raised
```

## Sets
---
Sets are unordered collections of `unique` elements. Meaning there can only be one representative of the same object.
```python
myset = set()

myset.add(1) # adds element to set
myset.add(2)
myset.add(2) # this element will not be added because '2' already is in the set. But no error will be raised

print(myset)

mylist = [1,5,1,1,1,1,1,1,2,2,2,2,3,4,4]
uniquevalues = set(mylist) # casts a list to set, eliminating all duplicated values

print(uniquevalues)
```

## Booleans
---
Booleans are operators that allow you to convey `True` or `False` statements. On python the value true/false are capitalized ( `True` / `False` )
```python
t = True
f = False

print(t)
print(type(t))
```

## Files I/O
---
Python allows to work with SO I/O.

### `Reading File | Old Way`
```python
filePath = '../artifacts/test.txt'
myfile = open(filePath) # opens file

content = myfile.read() # reads everything inside the file. Returning a single string
print(content)
content = myfile.read() # this will return an empty string, since right now the cursor is at the end of the file
print(content)
myfile.seek(0) # resets the cursor to the beggining of the file
content = myfile.read()
print(content)

myfile.seek(0)
print(myfile.readlines()) # returns an array with each element represents the line of the file

myfile.close() # closes file
```

### `Reading File | New Way`
```python
filePath = '../artifacts/test.txt'

# new way to handle file, using with it is not necessary to close the file
with open(filePath) as my_new_file:
  content2 = my_new_file.read()

print(content2)
```
### `File Mode`
By the default python opens the file as read, however it is possible to configure it using a custom mode
- `mode="r"` is read only
- `mode="w"` is write only (will overwrite files or create new one)
- `mode="a"` is append only (will add on to files)
- `mode="r+"` is reading and writing 
- `mode="w+"` is writing and reading (Overwrites existing files or creates a new one)
```python
filePath = '../artifacts/test.txt'
# opening as read
with open(filePath, mode='r') as my_new_file: 
  content = my_new_file.read()
print(content)

# opening as append
with open(filePath, mode = 'a') as myfile:
  myfile.write('\nthis is a new line')

# opening as read and write
with open(filePath, mode='r+') as my_new_file: 
  content = my_new_file.read()
print(content)

# Creates a text file if not exists
with open('../artifacts/test2.txt', mode = 'w') as myfile:
  myfile.write('Creates a new text file')
```

## References
---

- [`String Format Examples`](https://pyformat.info/)
- [`Basic Practice`](http://codingbat.com/python)
- [`List of Practice Problems`](http://www.codeabbey.com/index/task_list) 
- [`Python Challenges`](http://www.pythonchallenge.com/)
