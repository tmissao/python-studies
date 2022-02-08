# Python Packages

`PyPI` is a repository for open-source third-party Python packages similar to maven for Java and npm for Node.js

## Installing External Packages using command line
---

```bash
# pip3 install <package-name>
pip3 install colorama
```

```python
from colorama import init
init()
from colorama import Fore

print(f'{Fore.RED} red for my text')
```

## Internal Modules
---

This is an approach for utilize code from different files

```python
# ./mymodule.py
def my_func():
  print('Hey I am in mymodule.py')

# ./myprogram.py
# imports code from other file, in this case, imports the function my_func from mymodule.py
from mymodule import my_func
my_func()
```

## Packages
---
On python a package is defined using a folder and a special file called `__init__.py` inside this folder. Using this structure python is enable to understand that the folder is a package. Also the same rule applies to subpackages

> Nothing needs to be added into `__init__.py` file

```bash
.
├── main.py
└── package
    ├── __init__.py # defines package as a python package
    ├── script.py
    └── subpackage
        ├── __init__.py
        └── subscript.py
```
```python
# package/script.py
def report():
  print('Script from package')

# package/subpackage/subscript.py
def report():
  print('Script from subpackage')

# main.py
# imports package in the same directory level
from package import script
# imports subpackage from package
from package.subpackage import subscript

script.report()
subscript.report()


```