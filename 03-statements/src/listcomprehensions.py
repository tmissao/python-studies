mylist = []

# Long way for
for e in range(11):
  mylist.append(e)

print(mylist)

# shorter for using list comprehension
mylist = [ e for e in range(11) ]
print(mylist)

# shorter for with condition filter (just get even number)
even = [ e for e in range(11) if e % 2 == 0 ]
print(even)

# shorter for with condition filter (just get odd number) and return logic (power of the element)
odd_pow = [ e ** 2 for e in range(11) if e % 2 == 1 ] 
print(odd_pow)

# shorter if else logic
even_or_odd = [ 'even' if e % 2 == 0 else 'odd' for e in range(11) ]
print(even_or_odd)

# celsius  to fahrenheit
celsius  = [0, 10, 20, 34.5]
fahrenheit = [ ( (9/5)*e + 32 ) for e in celsius  ]
print(fahrenheit)

# nested for
mylist = []
for x in [2,4,6]:
  for y in [1,10,100]:
    mylist.append(x*y)
print(mylist)

# shorter nested for
mylist = [ x*y for x in [2,4,6] for y in [1,10,100] ]
print(mylist)