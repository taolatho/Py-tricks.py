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
