# Python Basic

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

## References
---

- [`String Format Examples`](https://pyformat.info/)