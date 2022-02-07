class Dog():

  # Class Object Attribute, same for any instance of Class
  species = 'mammal'
  
  # constructor, always called when class is created
  # self references the instance being created
  def __init__(self, breed, name):
      # Attributes
      self.breed = breed
      self.name = name
  
  # method
  # self connects the instance with the method
  # Dog.attribute is usually used to access class object attribute, but it is possible to use self also
  def bark(self, number = 1):
    for _ in range(number): 
      print(f'WooF! My name is {self.name} and I my specie is {Dog.species}')

  def get_name(self):
    return self.name


my_dog1 = Dog(breed='Lab', name='Farofa')
my_dog2 = Dog('Canine', 'Fox')


print(my_dog1.breed)
print(my_dog2.breed)

print(my_dog1.species)
print(my_dog2.species)

my_dog1.bark()
my_dog2.bark(3)