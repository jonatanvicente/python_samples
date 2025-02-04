

'''
     - ordered
     - immutable
     - better performance than lists
     - allows duplicates
'''

# Initializing a tuple
my_tuple = (1, 2, 3, 4, 5)

# 1. Accessing an element by index
element = my_tuple[0]
print(element)  # Output: 1

# 2. Counting occurrences of an element
count = my_tuple.count(3)
print(count)  # Output: 1

# 3. Finding the index of an element
index = my_tuple.index(4)
print(index)  # Output: 3

# 4. Slicing a tuple
sliced_tuple = my_tuple[1:4]
print(sliced_tuple)  # Output: (2, 3, 4)

# 5. Concatenating tuples
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)

# 6. Unpacking a tuple
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5

# 7. Checking if an element exists
exists = 3 in my_tuple
print(exists)  # Output: True

# 8. Getting the length of a tuple
length = len(my_tuple)
print(length)  # Output: 5

# 9. Iterating through a tuple
for item in my_tuple:
    print(item)
# Output:
# 1
# 2
# 3
# 4
# 5

# 10. Creating a tuple with a single element
single_element_tuple = (1,)
print(single_element_tuple)  # Output: (1,)