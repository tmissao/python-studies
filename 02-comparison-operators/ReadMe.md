# Comparison Operators

- Equality (==)
```python
1 == 1 # true
2 == 1 # false
'hello' == 'bye' # false
'Bye' == 'bye' # false
'2' == 2 # false
2.0 == 2 # true
```
- Inequality (!=)
```python
1 != 1 # false
2 != 1 # true
```

- Greater (>)
```python
1 != 1 # false
2 != 1 # true
```
- Greater than (>=)
```python
1 >= 1 # true
2 >= 1 # true
```
- Less (<)
```python
1 < 1 # false
0 < 1 # true
```
- Less than (>=)
```python
1 <= 1 # true
0 < 1 # true
```

# Logical Operators

- and (requires both conditions to be true)
```python
1 < 2 and 2 > 3 # false
1 < 2 and 2 < 3 # true
```

- or
```python (requires just one condition to be true)
1 < 2 or 2 > 3 # true
1 < 2 or 2 < 3 # true
```

- not
```python (returns the opposite of the condition)
not(1 == 1) # false
not 2 < 1 # true
```