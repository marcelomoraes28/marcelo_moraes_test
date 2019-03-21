
StringLib
=======================================

What is StringLib?
----------------------------------

StringLib is a python library to compare the size of two strings.

How can I use?
-------------

Possible returns:
- x is greater than y
- x is less than y
- x is equal to y

**Rules:**
- If the two entries are of the same type, the library will convert them to the type and then compare;
- If one of the two entries is string, the library will convert the both of them to string and then compare;
- The entries must be string Eg: '1.2', 'abc', '124', '[]A2';

Installing
-------------
```
pip install string_lib
```
Quick start
-----------
**Examples**

```python
from string_lib import StringLib

print(StringLib.which_size('1.4', '1.2'))
# output: 1.4 is greater than 1.2

print(StringLib.which_size('1.2', '1.4a'))
# output: 1.2 is less than 1.4a

print(StringLib.which_size('2.2c', '2222'))
# output: 2.2c is equal to 2222

```

Run tests
------------
In the question_b dir you should run:
```
pytest -ra
```
