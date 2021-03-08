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
