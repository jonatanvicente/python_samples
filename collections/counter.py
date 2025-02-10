'''
A dictionary subclass for counting hashable objects.
It is used to count the occurrences of elements in an iterable.
'''
from collections import Counter

# Create a Counter
c = Counter('gallahad')
print(c)  # Output: Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})