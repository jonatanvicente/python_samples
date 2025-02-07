'''
A deque (double-ended queue) is a data structure from the collections
module in Python that allows you to add and remove elements from both
ends efficiently. It is optimized for fast fixed-time append and pop
operations from both the left and right sides.
'''

from collections import deque

# Create a deque
d = deque([1, 2, 3])
d.append(4)         # Add to the right end
d.appendleft(0)     # Add to the left end
print(d)            # Output: deque([0, 1, 2, 3, 4])

# Remove elements
d.pop()             # Remove from the right end
d.popleft()         # Remove from the left end
print(d)            # Output: deque([1, 2, 3])