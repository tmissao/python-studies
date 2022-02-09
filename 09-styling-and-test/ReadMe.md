# Styling

Python uses a set of rules called PEP 8, it dictates python styles like, name conventions, design patterns etc. A tool used to validate these rules is `Pylint` 

## Installing Pylint
---

```bash
pip3 install pylint
```

## Evaluation Code with Pylint

```python
# demo_pylint.py
a,b = 1,2

print(f'the value of a is {a}, the value of b is {B}')
```

```bash
# basic report
pylint demo_pylint.py

# ************* Module demo-pylint
# demo_pylint.py:3:0: C0304: Final newline missing (missing-final-newline)
# demo_pylint.py:1:0: C0103: Module name "demo-pylint" doesn't conform to snake_case naming style (invalid-name)
# demo_pylint.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# demo_pylint.py:3:50: E0602: Undefined variable 'B' (undefined-variable)
# 
# -------------------------------------
# Your code has been rated at -30.00/10

# detailed report
pylint demo_pylint.py -r y

# ************* Module demo-pylint
# demo_pylint.py:3:0: C0304: Final newline missing (missing-final-newline)
# demo_pylint.py:1:0: C0103: Module name "demo-pylint" doesn't conform to snake_case naming style (invalid-name)
# demo_pylint.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# demo_pylint.py:3:50: E0602: Undefined variable 'B' (undefined-variable)
# 
# 
# Report
# ======
# 2 statements analysed.
# 
# Statistics by type
# ------------------
# 
# +---------+-------+-----------+-----------+------------+---------+
# |type     |number |old number |difference |%documented |%badname |
# +=========+=======+===========+===========+============+=========+
# |module   |1      |1          |=          |0.00        |100.00   |
# +---------+-------+-----------+-----------+------------+---------+
# |class    |0      |NC         |NC         |0           |0        |
# +---------+-------+-----------+-----------+------------+---------+
# |method   |0      |NC         |NC         |0           |0        |
# +---------+-------+-----------+-----------+------------+---------+
# |function |0      |NC         |NC         |0           |0        |
# +---------+-------+-----------+-----------+------------+---------+
# 
# 
# 
# Raw metrics
# -----------
# 
# +----------+-------+------+---------+-----------+
# |type      |number |%     |previous |difference |
# +==========+=======+======+=========+===========+
# |code      |3      |60.00 |NC       |NC         |
# +----------+-------+------+---------+-----------+
# |docstring |0      |0.00  |NC       |NC         |
# +----------+-------+------+---------+-----------+
# |comment   |0      |0.00  |NC       |NC         |
# +----------+-------+------+---------+-----------+
# |empty     |2      |40.00 |NC       |NC         |
# +----------+-------+------+---------+-----------+
# 
# 
# 
# Duplication
# -----------
# 
# +-------------------------+------+---------+-----------+
# |                         |now   |previous |difference |
# +=========================+======+=========+===========+
# |nb duplicated lines      |0     |0        |0          |
# +-------------------------+------+---------+-----------+
# |percent duplicated lines |0.000 |0.000    |=          |
# +-------------------------+------+---------+-----------+
# 
# 
# 
# Messages by category
# --------------------
# 
# +-----------+-------+---------+-----------+
# |type       |number |previous |difference |
# +===========+=======+=========+===========+
# |convention |3      |3        |3          |
# +-----------+-------+---------+-----------+
# |refactor   |0      |0        |0          |
# +-----------+-------+---------+-----------+
# |warning    |0      |0        |0          |
# +-----------+-------+---------+-----------+
# |error      |1      |1        |1          |
# +-----------+-------+---------+-----------+
# 
# 
# 
# Messages
# --------
# 
# +-------------------------+------------+
# |message id               |occurrences |
# +=========================+============+
# |undefined-variable       |1           |
# +-------------------------+------------+
# |missing-module-docstring |1           |
# +-------------------------+------------+
# |missing-final-newline    |1           |
# +-------------------------+------------+
# |invalid-name             |1           |
# +-------------------------+------------+
# 
# 
# 
# 
# ----------------------------------------------------------------------
# Your code has been rated at -30.00/10 (previous run: -30.00/10, +0.00)
```

# Running Tests

Unit tests it is a great way to stress your code and ensure that it really works. In python test cases could be created easily inherited the `unittest.TestCase` class

```python
# ./unittest/cap.py
def cap_text(text):
  return text.title()

# ./unittest/test_cap.py
import unittest
import cap

class TestCap(unittest.TestCase):
  def test_one_word(self):
    text = 'python'
    result = cap.cap_text(text)
    expect = 'Python'
    self.assertEqual(result, expect)

  def test_multiple_words(self):
    text = 'python rocks!'
    result = cap.cap_text(text)
    expect = 'Python Rocks!'
    self.assertEqual(result, expect)

if __name__ == '__main__':
  unittest.main()
```

```bash
python3 test_cap.py
```