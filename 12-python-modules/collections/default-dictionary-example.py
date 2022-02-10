from collections import defaultdict

# uses a lambda function to set a default value
d = defaultdict(lambda: 0)

d['correct'] = 100

print(f'the value of correct is: {d["correct"]}')

# On default dict this will raised an error 
print(f'the value of wrong is: {d["wrong"]}')