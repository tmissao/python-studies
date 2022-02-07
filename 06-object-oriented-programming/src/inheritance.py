# Base Class
class Animal():
  
  def __init__(self):
    print('Animal Created')
  
  def who_am_i(self):
    print('I am an animal')

  def eat(self):
    print('I am eating')

# Child Class
# The inheritance is defined passing the class inside the parenthesis during class declaration
class Dog(Animal):

  # overwrites parent constructor
  def __init__(self):
    # since parent constructor was overwrote it is necessary to invoke it using
    # the super() method. Super() return the reference of the parent class
    super().__init__()
    # Another way to do it is:
    # Animal.__init__(self)
    print('Dog Created')

  # overwrites method
  def who_am_i(self):
    print('I am a dog!')

  def bark(self):
    print('Woof!')

my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()

my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()
my_dog.bark()
