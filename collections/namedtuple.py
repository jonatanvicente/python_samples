'''
A factory function for creating tuple subclasses with named fields.
It allows for creating simple classes with fields that can be accessed by name.
'''

from collections import namedtuple

# Define a named tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
print(p.x, p.y)  # Output: 11 22


