from collections import namedtuple
from unicodedata import name

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

