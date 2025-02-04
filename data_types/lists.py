# Initializing a list
my_list = [1, 2, 3, 4, 5]

# 1. Append - Adds an element to the end of the list
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# 2. Extend - Adds all elements of a list to the end of the current list
my_list.extend([7, 8])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# 3. Insert - Inserts an element at a specified position
my_list.insert(0, 0)
print(my_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# 4. Remove - Removes the first occurrence of an element
my_list.remove(3)
print(my_list)  # Output: [0, 1, 2, 4, 5, 6, 7, 8]

# 5. Pop - Removes and returns the element at the specified position
popped_element = my_list.pop(0)
print(popped_element)  # Output: 0
print(my_list)  # Output: [1, 2, 4, 5, 6, 7, 8]

# 6. Clear - Removes all elements from the list
my_list.clear()
print(my_list)  # Output: []

# Re-initializing the list for further examples
my_list = [1, 2, 3, 4, 5]

# 7. Index - Returns the index of the first occurrence of an element
index = my_list.index(3)
print(index)  # Output: 2

# 8. Count - Returns the number of occurrences of an element
count = my_list.count(3)
print(count)  # Output: 1

# 9. Sort - Sorts the list in ascending order
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4, 5]

# 10. Reverse - Reverses the elements of the list
my_list.reverse()
print(my_list)  # Output: [5, 4, 3, 2, 1]

# 11. Copy - Returns a shallow copy of the list
copied_list = my_list.copy()
print(copied_list)  # Output: [5, 4, 3, 2, 1]