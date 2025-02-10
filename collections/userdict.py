'''
A wrapper around dictionary objects for easier dictionary subclassing.
It allows for creating custom dictionary-like classes.
'''
from collections import UserDict

# Create a UserDict
class MyDict(UserDict):
    def __setitem__(self, key, value):
        if isinstance(key, str):
            super().__setitem__(key, value)
        else:
            raise TypeError('Keys must be strings')

d = MyDict()
d['a'] = 1
print(d)  # Output: {'a': 1}