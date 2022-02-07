# Base Class / Abstract Class
class Animal:

  def __init__(self, name):
      self.name = name

  def speak(self):
    raise NotImplementedError('Subclass must implement this abstract method')

# Dog Class / Implements Animal
class Dog(Animal):

  def __init__(self, name):
      super().__init__(name)

  def speak(self):
      return f'{self.name} says bark!'

# Cat Class / Implements Animal
class Cat(Animal):

  def __init__(self, name):
      super().__init__(name)

  def speak(self):
      return f'{self.name} says meow!'

dog, cat = Dog('Farofa'), Cat('Simba')

# Polymorphism
def pet_speak(pet):
  print(pet.speak())

for e in [dog, cat]:
  pet_speak(e)
