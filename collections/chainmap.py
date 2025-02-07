'''
A class for creating a single view of multiple mappings (dictionaries).
It allows for searching through multiple dictionaries as if they were
a single one.
'''
from collections import ChainMap

# Create two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Create a ChainMap
chain = ChainMap(dict1, dict2)
print(chain['b'])  # Output: 2
print(chain['c'])  # Output: 4