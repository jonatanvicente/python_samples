'''
 The array module defines a sequence data structure that behaves very much like lists, except that
 all elements must be of the same type.
'''

import array

# Creating an array of integers
int_array = array.array('i', [1, 2, 3, 4, 5])
print(int_array)  # Output: array('i', [1, 2, 3, 4, 5])

# Accessing elements by index
print(int_array[0])  # Output: 1

# Appending an element
int_array.append(6)
print(int_array)  # Output: array('i', [1, 2, 3, 4, 5, 6])

# Inserting an element
int_array.insert(0, 0)
print(int_array)  # Output: array('i', [0, 1, 2, 3, 4, 5, 6])

# Removing an element
int_array.remove(3)
print(int_array)  # Output: array('i', [0, 1, 2, 4, 5, 6])

# Popping an element
popped_element = int_array.pop()
print(popped_element)  # Output: 6
print(int_array)  # Output: array('i', [0, 1, 2, 4, 5])

# Getting the length of the array
length = len(int_array)
print(length)  # Output: 5