
# set cannot contain lists

# Creating a set using curly braces
set1 = {1, 2, 3, 4, 5}
# {1 ,2, 3, 4, 5} is valid too, whith no assignment
print(set1)  # Output: {1, 2, 3, 4, 5}

# Creating a set using the set() function
set2 = set([6, 7, 8, 9, 10])
print(set2)  # Output: {6, 7, 8, 9, 10}

# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()

# Initializing a set
my_set = {1, 2, 3, 4, 5}

# 1. Adding an element
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# 2. Removing an element using remove
my_set.remove(6)
print(my_set)  # Output: {1, 2, 3, 4, 5}

# 3. Removing an element using discard
my_set.discard(5)
print(my_set)  # Output: {1, 2, 3, 4}

# 4. Removing and returning an arbitrary element using pop
popped_element = my_set.pop()
print(popped_element)  # Output: 1 (or any other element)
print(my_set)  # Output: {2, 3, 4}

# 5. Clearing all elements
my_set.clear()
print(my_set)  # Output: set()

# Re-initializing the set for further examples
my_set = {1, 2, 3, 4, 5}

# 6. Checking if an element exists
exists = 3 in my_set
print(exists)  # Output: True

# 7. Getting the length of the set
length = len(my_set)
print(length)  # Output: 5

# 8. Iterating through a set
for item in my_set:
    print(item)
# Output:
# 1
# 2
# 3
# 4
# 5

# 9. Union of sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# 10. Intersection of sets
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3}

# 11. Difference of sets
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}

# 12. Symmetric difference of sets
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# 13. Checking if a set is a subset
is_subset = set_a.issubset({1, 2, 3, 4, 5})
print(is_subset)  # Output: True

# 14. Checking if a set is a superset
is_superset = set_a.issuperset({1, 2})
print(is_superset)  # Output: True

# 15. Copying a set
copied_set = my_set.copy()
print(copied_set)  # Output: {1, 2, 3, 4, 5}

# 16. Updating a set with another set
my_set.update({6, 7})
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}