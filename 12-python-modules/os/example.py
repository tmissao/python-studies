import os
import shutil

demo_file_path = '../practice.txt'

with open(demo_file_path, 'w+') as f:
  f.write('This is a test string')

# Get current working directory
print(os.getcwd())

# Lists everything in the directory
print(os.listdir())

# Lists everything in the directory relative to the path received
print(os.listdir('../../'))

# Get environment variable
print(os.getenv('PATH'))

# Moves files
shutil.move(demo_file_path, 'practice.txt')

# Walks through directory tree
for folder, sub_folder, files in os.walk('../'):
  print(f'folder: {folder}')
  print(f'sub_folder: {sub_folder}')
  print(f'files: {files}')