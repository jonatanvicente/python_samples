'''
A dictionary subclass that calls a factory function to supply missing values.
It provides a default value for the key that does not exist.
'''

from collections import defaultdict

# Create a defaultdict
dd = defaultdict(int)
dd['a'] += 1
print(dd)  # Output: defaultdict(<class 'int'>, {'a': 1})