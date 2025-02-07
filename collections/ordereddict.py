'''
A dictionary subclass that remembers the order in which keys were first
inserted. It maintains the order of keys as they are added.
'''
from collections import OrderedDict

# Create an OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])