filePath = '../artifacts/test.txt'
myfile = open(filePath) # opens file

content = myfile.read() # reads everything inside the file. Returning a single string
print(content)
content = myfile.read() # this will return an empty string, since right now the cursor is at the end of the file
print(content)
myfile.seek(0) # resets the cursor to the beggining of the file
content = myfile.read()
print(content)

myfile.seek(0)
print(myfile.readlines()) # returns an array with each element represents the line of the file

myfile.close() # closes file


with open(filePath) as my_new_file: # new way to handle file, using with it is not necessary to close the file
  content2 = my_new_file.read()

print(content2)

# Open Files with modes

# opening as read
with open(filePath, mode='r') as my_new_file: 
  content = my_new_file.read()
print()
print(content)

# opening as append
with open(filePath, mode = 'a') as myfile:
  myfile.write('\nthis is a new line')

# opening as read and write
with open(filePath, mode='r+') as my_new_file: 
  content = my_new_file.read()
print()
print(content)

# Creates a text file if not exists
with open('../artifacts/test2.txt', mode = 'w') as myfile:
  myfile.write('Creates a new text file')

