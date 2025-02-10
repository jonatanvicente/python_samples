'''
A wrapper around list objects for easier list subclassing. It allows for creating custom list-like classes.
'''
from collections import UserList

# Create a UserList
class MyList(UserList):
    def append(self, item):
        if isinstance(item, int):
            super().append(item)
        else:
            raise TypeError('Items must be integers')

l = MyList([1, 2, 3])
l.append(4)
print(l)  # Output: [1, 2, 3, 4]