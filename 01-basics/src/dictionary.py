dict = { 'key1' : 'value1', 'key2' : 'value2' }

print(dict)
print(dict['key2']) # retrieves a value using the dictionary's key

d = { 'k1': 123, 'k2': [0,1,2], 'k3': {'insideKey': 1000}}
print(d['k1'])
print(d['k2'][2])
print(d['k3']['insideKey'])

d['k4'] = 300 # adds a new key-value on dictionary
d['k1'] = 200 # updates a value on dictionary
print(d)

# Dictionary methods
print(d.keys()) # returns all keys of the dictionary
print(d.values()) # returns all values of the dictionary
print(d.items()) # returns all key-value of the dictionary together