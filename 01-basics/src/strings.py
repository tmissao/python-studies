msg = 'hello'
msg2 = "Hello"
msg3 = "Hello \n world"

# Strings
print(msg)
print(msg2)
print(msg3)

# String Indexing
print("String Indexing")
print(msg[0])
print(msg[1])
print(msg[2])
print(msg[3])
print(msg[4])

print()

# Strings Reverse Indexing
print("String Reverse Indexing")
print(msg[-1]) # get the last element of the string
print(msg[-2])
print(msg[-3])
print(msg[-4])
print(msg[0])

print()
print("String Length")
print(len(msg2)) # returns the length of a string

# Slicing
print()
print ("String Slicing")
print(msg[1:]) # Substring starting on index 1
print(msg[1:3]) # Substring starting on index 1 and ending on 3 (not inclusive)
print(msg[:3]) # Substring starting on the beggining and ending on 3 (not inclusive)
print(msg[::2]) # Substring starting on the beggining to the end, but steping by two
print(msg[::-1]) # Reverses String

# Concatenation
print()
print ("String Concatenation")
name = "Sam"
print("P" + name[1:]) # String Concatenation

print()
print ("String Multiplication")
print(name * 3) # String Concatenation

print()
print ("String Methods")
print(name.upper()) # Upper Case String
print(name.lower()) # Lower Case String
print(name.split("a")) # split string into a list based on a specific value