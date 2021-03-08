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
