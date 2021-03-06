# Py-tricks 🐍
#### @Dan
### [Different ways to test multiple flags at once in Python](https://repl.it/@tphat98/Different-ways-to-test-multiple-flags-at-once-in-Python "Different ways to test multiple flags at once in Python")
```python
# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print("passed_1")  # passed_1

if 1 in (x, y, z):
    print("passed_2")  # passed_2

# These only test for truthiness:
if x or y or z:
    print("passed_3")  # passed_3

if any((x, y, z)):
    print("passed_4")  # passed_4
```
### [Function argument unpacking in Python](https://repl.it/@tphat98/Function-argument-unpacking-in-Python "Function argument unpacking in Python")
```python
# Why Python Is Great:
# Function argument unpacking


def myfunc(x, y, z):
    print(x, y, z)


tuple_vec = (1, 0, 1)
dict_vec = {"x": 1, "y": 0, "z": 1}

myfunc(*tuple_vec)  # 1 0 1

myfunc(**dict_vec)  # 1 0 1
```
### [How to create a countdown timer using Python?](https://repl.it/@tphat98/How-to-create-a-countdown-timer-using-Python "How to create a countdown timer using Python?")
```python
# import the time module
import time

# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Fire in the hole!!")


# function call
countdown(int(5))
```
### [How to print numbers with commas as thousands of separators?](https://repl.it/@tphat98/How-to-print-numbers-with-commas-as-thousands-of-separators "How to print numbers with commas as thousands of separators?")
```python
x = 1234567
# Locale unaware

# For Python ≥2.7
print("{:,.0f}".format(x))  # 1,234,567
print("{:,}".format(x))  # 1,234,567

# Python 3
## Integers (without decimal):
print("{:,d}".format(x))  # 1,234,567

## Floats (with decimal):
print("{:,.2f}".format(x))  # 1,234,567.00

# For Python ≥3.1
print(format(x, ",d"))  # 1,234,567

# For Python ≥3.6
print(f"{x:,}")  # 1,234,567

# Locale aware
import locale

# Use '' for auto, or force e.g. to 'en_US.UTF-8'
locale.setlocale(locale.LC_ALL, "")

# For Python ≥2.7
print("{:n}".format(x))  # 1,234,567

# For Python ≥3.6
print(f"{x:n}")  # 1,234,567
```
### [How to sort a Python dict by value?](https://repl.it/@tphat98/How-to-sort-a-Python-dict-by-value "How to sort a Python dict by value?")
```python
# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {"a": 4, "b": 3, "c": 2, "d": 1}
print(
    sorted(xs.items(), key=lambda x: x[1])
)  # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:
import operator

print(
    sorted(xs.items(), key=operator.itemgetter(1))
)  # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
```
### [Merging two dicts in Python 3.5+ with a single expression](https://repl.it/@tphat98/Merging-two-dicts-in-Python-35-with-a-single-expression "Merging two dicts in Python 3.5+ with a single expression")
```python
# How to merge two dictionaries
# in Python 3.5+

x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}

print({**x, **y})  # {'a': 1, 'b': 3, 'c': 4}


# In Python 2.x you could
# use this:
print(dict(x, **y))  # {'a': 1, 'b': 3, 'c': 4}

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting
# duplicates from left to right.
```
### [Python's namedtuples can be a great alternative to defining a class manually](https://repl.it/@tphat98/1 "Python's namedtuples can be a great alternative to defining a class manually")
```python
# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than
# defining a class manually:
from collections import namedtuple

Car = namedtuple("Car", "color mileage")

# Our new "Car" class works as expected:
my_car = Car("red", 3812.4)
print(my_car.color)  # red

print(my_car.mileage)  # 3812.4

# We get a nice string repr for free:
print(my_car)  # Car(color='red', mileage=3812.4)

# Like tuples, namedtuples are immutable:
my_car.color = "blue"
# AttributeError: "can't set attribute"
```
### [The get() method on Python dicts and its "default" arg](https://repl.it/@tphat98/The-get-method-on-Python-dicts-and-its-default-arg "The get() method on Python dicts and its default arg")
```python
# The get() method on dicts
# and its "default" argument

name_for_userid = {
    1: "Alice",
    2: "Bob",
    3: "Dilbert",
}


def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")


print(greeting(1))  # Hi Alice!
print(greeting(2))  # Hi Bob!
print(greeting(3))  # Hi Dilbert!
print(greeting(0))  # Hi there!
```
### [You can use "json.dumps()" to pretty-print Python dicts](https://repl.it/@tphat98/You-can-use-jsondumps-to-pretty-print-Python-dicts "You can use json.dumps() to pretty-print Python dicts")
```python
# The standard string repr for dicts is hard to read:
my_mapping = {"a": 23, "b": 42, "c": 0xC0FFEE}
print(my_mapping)  # {'a': 23, 'b': 42, 'c': 12648430}

# The "json" module can do a much better job:
import json

print(json.dumps(my_mapping, indent=4, sort_keys=True))
# {
#    "a": 23,
#    "b": 42,
#    "c": 12648430
# }

# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
json.dumps({all: "yup"})
# TypeError: keys must be a string
```
### [Measure the execution time of small bits of Python code with the "timeit" module](https://repl.it/@tphat98/Timeit-module "Measure the execution time of small bits of Python code with the timeit module")
```python
import timeit

# The "timeit" module lets you measure the execution
# time of small bits of Python code

# result
# 0-1-2-3-4-5-6-7-8-9-10...-99

print(
    timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
)  # 0.8995874719998938
print(
    timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
)  # 0.8709785030000603
print(
    timeit.timeit('"-".join(map(str, range(100)))', number=10000)
)  # 0.8709785030000603
```
### [Python's shorthand for in-place value swapping](https://repl.it/@tphat98/Pythons-shorthand-for-in-place-value-swapping "Python's shorthand for in-place value swapping")
```python
# Why Python Is Great:
# In-place value swapping

# Let's say we want to swap
# the values of a and b...
a = 1
b = 2
print(a, b)  # 1 2

# The "classic" way to do it
# with a temporary variable:
tmp = a
print(tmp)  # 1

a = b
print(a)  # 2

b = tmp
print(b)  # 1

print(a, b, tmp)  # 2 1 1

# Python also lets us
# use this short-hand:
a, b = b, a

print(a, b)  # 1 2
```
### ["is" vs "=="](https://repl.it/@tphat98/is-vs "is vs ==")
```python
# "is" vs "=="
a = [1, 2, 3]

b = a
print(a is b)  # True
print(a == b)  # True

c = list(a)
print(a is c)  # False
print(a == c)  # True

# "is" expressions evaluate to True if two
# variables point to the same object

# "==" evaluates to True if the objects
# referred to by the variables are equal
```
### [Functions are first-class citizens in Python](https://repl.it/@tphat98/Functions-are-first-class-citizens-in-Python "Functions are first-class citizens in Python")
```python
# Functions are first-class citizens in Python:

# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.


def myfunc(a, b):
    return a + b


print(myfunc(1, 2))  # 3

funcs = [myfunc]
print(funcs[0])  # <function myfunc at 0x7fad6b1d51f0>
print(funcs[0](3, 4))  # 7
```
### [Dicts can be used to emulate switch/case statements](https://repl.it/@tphat98/Dicts-can-be-used-to-emulate-switchcase-statements "Dicts can be used to emulate switch/case statements")
```python
# Because Python has first-class functions they can
# be used to emulate switch/case statements


def dispatch_if(operator, x, y):
    if operator == "add":
        return x + y
    elif operator == "sub":
        return x - y
    elif operator == "mul":
        return x * y
    elif operator == "div":
        return x / y
    else:
        return None


def dispatch_dict(operator, x, y):
    return {
        "add": lambda: x + y,
        "sub": lambda: x - y,
        "mul": lambda: x * y,
        "div": lambda: x / y,
    }.get(operator, lambda: None)()


print(dispatch_if("mul", 2, 8))  # 16
print(dispatch_dict("mul", 2, 8))  # 16
print(dispatch_if("unknown", 2, 8))  # None
print(dispatch_dict("unknown", 2, 8))  # None
```
### Python's built-in HTTP server
```
# Python has a HTTP server built into the
# standard library. This is super handy for
# previewing websites.

# Python 3.x
$ python3 -m http.server

# Python 2.x
$ python -m SimpleHTTPServer 8000

# (This will serve the current directory at
#  http://localhost:8000)
```
### [Python's list comprehensions are awesome](https://repl.it/@tphat98/Pythons-list-comprehensions-are-awesome "Python's list comprehensions are awesome")
```python
# Python's list comprehensions are awesome.

vals = [expression 
        for value in collection 
        if condition]

# This is equivalent to:

vals = []
for value in collection:
    if condition:
        vals.append(expression)

# Example:
even_squares = [x * x for x in range(10) if not x % 2]
print(even_squares)  # [0, 4, 16, 36, 64]
```
