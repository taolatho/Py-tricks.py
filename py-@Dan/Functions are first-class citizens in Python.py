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
