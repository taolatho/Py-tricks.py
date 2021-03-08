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
