from collections import Counter
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