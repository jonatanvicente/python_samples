'''
A wrapper around string objects for easier string subclassing. It allows for creating custom string-like classes.
'''
from collections import UserString

# Create a UserString
class MyString(UserString):
    def append(self, s):
        self.data += s

s = MyString("Hello")
s.append(" World")
print(s)  # Output: Hello World