name = "Tiago"
surname = "Missão"
result = 0.1287001287001287

print('Hello my first name is {}, and my last name is {}'.format(name, surname))

# The '{}' is evaluated in order by default
print('The {} {} {}'.format('fox', 'brown', 'quick'))

# The '{}' can be accessed using indexing
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))

# The '{}' can use keywords to retrieve values
print('The {f} {b} {q}'.format(f='fox', b='brown', q='quick'))

# Formating floating numbers "{value:width.precision f}"
print('The result is: {r:1.3f}'.format(r=result))


# f-strings
print(f'Hello my first name is {name}, and last name {surname}')
print(f'the result is {result:1.3f}')